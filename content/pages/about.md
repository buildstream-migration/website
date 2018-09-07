title: About BuildStream
slug: about

<!-- This page explains what the BuildStream project do and the project outcomes: Master (including dev snapshots) and releases. It will also talk about BuildGrid and mention the relation with freedesktop-sdk when it comes to outcomes -->

<!-- For the release badges, check https://gitlab.com/BuildStream/website/issues/3 -->

<!-- Short explanation about what the BuildStream project ships (outcomes) and who they are for: snapshots, releases and master  -->
The BuildStream project develops, delivers and maintains an integration toolset called BuildStream specially designed for software application developers and integrators of complex systems that follow modern delivery methodologies to ship software that should be in production for a long time. At the same time, as Free Software project, BuildStream ships versions of the tools set advancing the features that will be shipped in the future for those who want to evaluate where the toolset is heading or test them. Finally, BuildStream toolset development mostly takes place in the master branch of the buildstream repository, which the project refers to as Master.

We provide:

* BuildStream releases, for software application developers and system integrators.
* Development snapshots, for BuilStream testers and users who are interested in evaluating what's coming.
* Master, for contributors who participate in the BuildStream development.

BuildStream relies on a sister project in order to be able to build at scale, called BuildGrid.

## Building applications and integrating systems

<!-- Releases: description. Who is for. State clearly which one is the latest release. -->

BuildStream releases are "ready to use" versions, that will receive maintenance patches and security fixes for some time. Releases are recommended for those who need a version of BuildStream for production environments.

Currently, the latest BuildStream release is <object style="vertical-align: middle" data="https://buildstream.gitlab.io/buildstream/_static/release.svg" type="image/svg+xml"></object>.

In order to learn more about this specific release, the following links will be of help:

* The publication of BuildStream releases is announced on this website through a [Release Announcement](articles/2018/buildstream-1.2-is-out/).
* You can find [What's New]({filename}feature_page.md) on each release by reading the release feature page, which includes also relevant information for those who want to consider installing BuildStream for the very first time.
* In order to Download and Install/Deploy BuildStream the next recommended step is to visit the [releases page]({filename}releases.md) and the [Installation and Deployment Instructions]({filename}installation.md) which will provide you a step by step guidance on the process.
* If you encounter any problem through this process, please visit the [Known Issues]({filename}known_issues.md) page. Hopefully you will find your problem described there together with a workaround to overcome it while the BuildStream developers fix the issue. A link to the issue tracker will allow you to follow the progress on it.
* Finally, the recommendation is to visit the [FAQ]({filename}faq.md#use-buildstream) (Frequently Asked Questions) page in order to find out more about BuildStream, how to get in contact with those who might help you, where can I find examples of how to use the tool and further interesting information.

A more technical and detailed description of BuildStream features, architecture, components, etc. can be found in [BuildStream In Detail]({filename}buildstream_in_detail.md).

## Latest features

BuildStream delivers Development Snapshots regularly for developers and integrators interested in evaluating what is coming and testing it. These snapshots are announced through the BuildStream community mailing list. These snapshots include those developed features that will be shipped in the next BuildStream Release that require validation or will benefit from further testing. But it is not a specific version for testers but an early version of what will be released later on.

Currently the latest Development Snapshot is <object style="vertical-align: middle" data="https://buildstream.gitlab.io/buildstream/_static/snapshot.svg" type="image/svg+xml"></object>.

If you are interested in these Development Snapshots we recommend you the following:

* [Find the Snapshot]({filename}releases.md#development-snapshots) you are interested on. We strongly recommend the latest one.
* Download it and [Install/Deploy]({filename}installation.md#installing) it or update it if you already have a previous snapshot installed. Visit the [Known Issues]({filename}known_issues.md) page if you have any issue during the installation or deployment process.
* Go to the [specific section of the FAQ]({filename}faq.md#contribute-to-buildstream) where you will find how to reach out to the developers, get the code or open a bug in case you detect an issue and want to report.

## Developing BuildStream

<!-- Description about what you can find in Master and who is for (contributors) -->

BuildStream is a welcoming Free Software project so your participation is one of the project goals. The toolset development takes place on [Gitlab.com](https://gitlab.com/BuildStream) and the main repository is called [buildstream](https://gitlab.com/BuildStream/buildstream). The development happens on Master. Following modern delivery practices, Master should always work.

If you are interested in contributing to the development of BuildStream or please check the [Participate in the BuildStream Project]({filename}community.md#participate-in-the-buildstream-project) section of the Community page.

## Semantic Versioning

BuildStream deliverable versions follow the Semantic Versioning Convention ([SemVer](https://semver.org/)) and uses even minor point numbers to denote BuildStream Releases while odd minor point numbers represent Development Snapshops.

For example, for a given version number `X.Y.Z`

* The `X.<even number>.*` versions are BuildStream Releases.
* The `X.<odd number>.*` versions are Development Spanshots.

If you are [installing from git]({filename}source_installation.md#install_git), please look for the latest tag to ensure you're getting the latest release.

## Links

<!--  Link section: links to important content for those who might be thinking about becoming users. Provide context for each link, at least a sentence. -->

* To learn more about the Free Software community aspects of the BuildStream project, visit the [Community page]({filename}community.md).
* To learn more about the promotion activities the BuildStream project does and their impact please visit BuildStream Out There (coming soon).
* [BuildGrid](https://gitlab.com/BuildGrid/buildgrid) is a remote execution service. The project's goal is to be able to execute build jobs remotely on a grid of computers in order to massively speed up build times. It is designed to work with but not exclusively BuildStream.