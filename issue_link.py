import json
import urllib

from markdown.extensions import Extension
from markdown.inlinepatterns import Pattern
from markdown.util import etree


# This plugin will create links to GitLab issues and merge requests
# for wikilinks written in the following format:
#
#     [[BuildStream/buildstream!737]]
#
# This would for example create the following link:
#
#     <a href="https://gitlab.com/BuildStream/buildstream/merge_requests/737" title="Tristan/restore post merge ci">!737 (merged)</a>
#
# The status of the given ticket will be indicated in brackets, unless
# GitLab API cannot be reached. In such a case, a best effort will be
# made to provide a correct URL, but no additional features beyond a
# nicer link format will be available.
#
LINK_RE = r'\[\[([a-z0-9.\-_\/]+)([#!])(\d+)\]\]'


class GitLabRequest():
    GITLAB_API = "https://gitlab.com/api/v4"

    @classmethod
    def _open_url(cls, url):
        with urllib.request.urlopen(cls.GITLAB_API + '/' + url) as response:
            # json.load(response) is only supported in >=python3.6
            issue = json.loads(response.read().decode('utf-8'))

        return issue

    @classmethod
    def issueopen(cls, project_id, issue):
        url = "projects/{}/issues/{}".format(project_id, issue)
        return cls._open_url(url)

    @classmethod
    def mropen(cls, project_id, merge_request):
        url = "projects/{}/merge_requests/{}".format(project_id, merge_request)
        return cls._open_url(url)


class IssueLink(Extension):
    def extendMarkdown(self, md, md_globals):
        issue_pattern = IssuePattern(LINK_RE)
        md.inlinePatterns.add('issue', issue_pattern, '>not_strong')


class IssuePattern(Pattern):
    def handleMatch(self, m):
        # If we can't parse the link, we just concatenate the groups
        link = '{}{}{}'.format(m.group(2), m.group(3), m.group(4))

        # Ensure that we actually have a non-empty match
        if (m.group(2) and m.group(2).strip() and
                m.group(3) and m.group(3).strip() and
                m.group(4) and m.group(4).strip()):

            # Parse the matches
            repository = urllib.parse.quote(m.group(2).strip(), safe='')
            kind = m.group(3).strip()
            identifier = int(m.group(4).strip())

            # Ask gitlab.com for info
            try:
                if kind == '#':
                    info = GitLabRequest.issueopen(repository, identifier)
                elif kind == '!':
                    info = GitLabRequest.mropen(repository, identifier)
            except urllib.error.URLError:
                # If we fail to query the GitLab API, we want to have
                # some form of default behavior.
                info = None

            # Build the link
            link = etree.Element('a')
            link.text = "{}{}".format(kind, identifier)

            # If we successfully query GitLab API, we use the
            # information provided.
            if info:
                if info['state'] != 'opened':
                    link.text += ' ({})'.format(info['state'])
                link.set('href', info['web_url'])
                link.set('title', info['title'])

            # If we fail to query GitLab API, we build a link manually
            # - hoping that this format is still correct.
            else:
                url = 'https://gitlab.com/{}/{}/{}'.format(
                    repository,
                    'issues' if kind == '#' else 'merge_requests',
                    identifier
                )
                link.set('href', url)

        return link
