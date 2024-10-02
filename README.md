# takelage-dev

*takelship* is a podman container runtime environment for docker with minimal footprint.

At the moment, these setups have been tested:
 - [Docker Engine for Linux (Debian)](https://docs.docker.com/engine/install/debian/) (amd64 and arm64)
 - [Docker Desktop for Linux (Debian)](https://docs.docker.com/desktop/install/linux/debian/) (amd64)
 - [Docker Desktop for macOS](https://docs.docker.com/desktop/install/mac-install/) (arm64)

You have to run docker as user, not as root. It is not possible to run the *takelship* container with podman although (or because?) it uses itself podman to run containers.

## Framework Versions

| Project | Artifacts |
|-|-|
| [![takelage-doc](https://img.shields.io/badge/github-takelage--doc-purple)](https://github.com/takelwerk/takelage-doc) | [![License](https://img.shields.io/badge/license-GNU_GPLv3-blue)](https://github.com/takelwerk/takelage-doc/blob/main/LICENSE) |
| [![takelage-var](https://img.shields.io/badge/github-takelage--var-purple)](https://github.com/takelwerk/takelage-var) | [![pypi,org](https://img.shields.io/pypi/v/pytest-takeltest?label=pypi.org&color=blue)](https://pypi.org/project/pytest-takeltest/) |
| [![takelage-cli](https://img.shields.io/badge/github-takelage--cli-purple)](https://github.com/takelwerk/takelage-cli) | [![rubygems.org](https://img.shields.io/gem/v/takeltau?label=rubygems.org&color=blue)](https://rubygems.org/gems/takeltau) |
| [![takelage-img-takelslim](https://img.shields.io/badge/github-takelage--img--takelslim-purple)](https://github.com/takelwerk/takelage-img-takelslim) | [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelslim/latest-amd64?label=hub.docker.com&arch=amd64&color=teal)](https://hub.docker.com/r/takelwerk/takelslim) [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelslim/latest-arm64?label=hub.docker.com&arch=arm64&color=slateblue)](https://hub.docker.com/r/takelwerk/takelslim) | 
| [![takelage-img-takelbase](https://img.shields.io/badge/github-takelage--img--takelbase-purple)](https://github.com/takelwerk/takelage-img-takelbase) | [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelbase/latest-amd64?label=hub.docker.com&arch=amd64&color=teal)](https://hub.docker.com/r/takelwerk/takelbase) [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelbase/latest-arm64?label=hub.docker.com&arch=arm64&color=slateblue)](https://hub.docker.com/r/takelwerk/takelbase) |
| [![takelage-img-takelpodslim](https://img.shields.io/badge/github-takelage--img--takelpodslim-purple)](https://github.com/takelwerk/takelage-img-takelpodslim) | [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelpodslim/latest-amd64?label=hub.docker.com&arch=amd64&color=teal)](https://hub.docker.com/r/takelwerk/takelpodslim) [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelpodslim/latest-arm64?label=hub.docker.com&arch=arm64&color=slateblue)](https://hub.docker.com/r/takelwerk/takelpodslim) | 
| [![takelage-img-takelpodbase](https://img.shields.io/badge/github-takelage--img--takelpodbase-purple)](https://github.com/takelwerk/takelage-img-takelpodbase) | [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelpodbase/latest-amd64?label=hub.docker.com&arch=amd64&color=teal)](https://hub.docker.com/r/takelwerk/takelpodbase) [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelpodbase/latest-arm64?label=hub.docker.com&arch=arm64&color=slateblue)](https://hub.docker.com/r/takelwerk/takelpodbase) | 
| [![takelage-dev](https://img.shields.io/badge/github-takelage--dev-purple)](https://github.com/takelwerk/takelage-dev) | [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelage/latest-amd64?label=hub.docker.com&arch=amd64&sort=semver&color=teal)](https://hub.docker.com/r/takelwerk/takelage) [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelage/latest-arm64?label=hub.docker.com&arch=arm64&sort=semver&color=slateblue)](https://hub.docker.com/r/takelwerk/takelage) |
| [![takelage-pad](https://img.shields.io/badge/github-takelage--pad-purple)](https://github.com/takelwerk/takelage-pad) | [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelpad/latest-amd64?label=hub.docker.com&arch=amd64&sort=semver&color=teal)](https://hub.docker.com/r/takelwerk/takelpad) [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelpad/latest-arm64?label=hub.docker.com&arch=arm64&sort=semver&color=slateblue)](https://hub.docker.com/r/takelwerk/takelpad) |
| [![takelship](https://img.shields.io/badge/github-takelship-purple)](https://github.com/takelwerk/takelship) | [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelship/latest-amd64?label=hub.docker.com&arch=amd64&sort=semver&color=teal)](https://hub.docker.com/r/takelwerk/takelship) [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelship/latest-arm64?label=hub.docker.com&arch=arm64&sort=semver&color=slateblue)](https://hub.docker.com/r/takelwerk/takelship) | |


## Framework Status

| Project | Pipelines |
|-|-|
| [![takelage-var](https://img.shields.io/badge/github-takelage--var-purple)](https://github.com/takelwerk/takelage-var) | [![takeltest](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-var/takeltest.yml?label=takeltest)](https://github.com/takelwerk/takelage-var/actions/workflows/takeltest.yml) [![test_takeltest](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-var/test_takeltest.yml?label=test%20takeltest)](https://github.com/takelwerk/takelage-var/actions/workflows/test_takeltest.yml) |
| [![takelage-cli](https://img.shields.io/badge/github-takelage--cli-purple)](https://github.com/takelwerk/takelage-cli) | [![takeltau](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-cli/takeltau.yml?label=takeltau)](https://github.com/takelwerk/takelage-cli/actions/workflows/takeltau.yml) [![test_takeltau](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-cli/test_takeltau.yml?label=test%20takeltau)](https://github.com/takelwerk/takelage-cli/actions/workflows/test_takeltau.yml) |
| [![takelage-img-takelslim](https://img.shields.io/badge/github-takelage--img--takelslim-purple)](https://github.com/takelwerk/takelage-img-takelslim) | [![takelslim amd64](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-img-takelslim/takelslim_amd64.yml?label=takelslim%20amd64)](https://github.com/takelwerk/takelage-img-takelslim/actions/workflows/takelslim_amd64.yml) |
| [![takelage-img-takelbase](https://img.shields.io/badge/github-takelage--img--takelbase-purple)](https://github.com/takelwerk/takelage-img-takelbase) | [![takelbase amd64](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-img-takelbase/takelbase_amd64.yml?label=takelbase%20amd64)](https://github.com/takelwerk/takelage-img-takelbase/actions/workflows/takelbase_amd64.yml) | 
| [![takelage-img-takelpodslim](https://img.shields.io/badge/github-takelage--img--takelpodslim-purple)](https://github.com/takelwerk/takelage-img-takelpodslim) | [![takelpodslim amd64](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-img-takelpodslim/takelpodslim_amd64.yml?label=takelpodslim%20amd64)](https://github.com/takelwerk/takelage-img-takelpodslim/actions/workflows/takelpodslim_amd64.yml) |
| [![takelage-img-takelpodbase](https://img.shields.io/badge/github-takelage--img--takelpodbase-purple)](https://github.com/takelwerk/takelage-img-takelpodbase) | [![takelpodbase amd64](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-img-takelpodbase/takelpodbase_amd64.yml?label=takelpodbase%20amd64)](https://github.com/takelwerk/takelage-img-takelpodbase/actions/workflows/takelpodbase_amd64.yml) | 
| [![takelage-dev](https://img.shields.io/badge/github-takelage--dev-purple)](https://github.com/takelwerk/takelage-dev) | [![takelage amd64](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-dev/takelage_amd64.yml?label=takelage%20amd64)](https://github.com/takelwerk/takelage-dev/actions/workflows/takelage_amd64.yml) [![test_takelage](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-dev/test_takelage.yml?label=test%20takelage)](https://github.com/takelwerk/takelage-dev/actions/workflows/test_takelage.yml) 
| | [![takelbuild amd64](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-dev/takelbuild_amd64.yml?label=takelbuild%20amd64)](https://github.com/takelwerk/takelage-dev/actions/workflows/takelbuild_amd64.yml) [![test_takelbuild](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-dev/test_takelbuild.yml?label=test%20takelbuild)](https://github.com/takelwerk/takelage-dev/actions/workflows/test_takelbuild.yml) |
| | [![takelbeta amd64](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-dev/takelbeta_amd64.yml?label=takelbeta%20amd64)](https://github.com/takelwerk/takelage-dev/actions/workflows/takelbeta_amd64.yml) [![test_roles](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-dev/test_roles.yml?label=test%20roles)](https://github.com/takelwerk/takelage-dev/actions/workflows/test_roles.yml) |
| [![takelage-pad](https://img.shields.io/badge/github-takelage--pad-purple)](https://github.com/takelwerk/takelage-pad) | [![takelpad docker](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-pad/takelpad_docker.yml?label=takelpad%20docker)](https://github.com/takelwerk/takelage-pad/actions/workflows/takelpad_docker.yml) |
| | [![test takelpad](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-pad/test_takelpad.yml?label=test%20takelpad)](https://github.com/takelwerk/takelage-pad/actions/workflows/test_takelpad.yml) [![test roles](https://img.shields.io/github/actions/workflow/status/takelwerk/takelage-pad/test_roles.yml?label=test%20roles)](https://github.com/takelwerk/takelage-pad/actions/workflows/test_roles.yml) |
| [![takelship](https://img.shields.io/badge/github-takelship-purple)](https://github.com/takelwerk/takelship) | [![takelship docker](https://img.shields.io/github/actions/workflow/status/takelwerk/takelship/takelship-amd64.yml?label=takelship%20docker)](https://github.com/takelwerk/takelship/actions/workflows/takelship-amd64.yml) |

## First steps

Get info how to run a takelship project:

```bash
docker run -it --rm takelwerk/takelship
```

Choose a project and run the respective command 
to run a takelship server:

```
$ docker run -it --rm takelwerk/takelship
[takelship] This is a takelwerk takelship container
[takelship] Image: takelwerk/takelship:0.1.42
[takelship] More info: https://github.com/takelwerk/takelship
[takelship] No project selected. Available projects:

== Project: all
= All services of all projects.
mkdir -p data && docker run --rm --interactive --tty --name takelship --hostname takelship --privileged --publish "35000:35000" --publish "30022:30022" --publish "33000:33000" --publish "38111:38111" --volume ./data:/home/podman/data takelwerk/takelship all

== Project: registry
= Docker registry (docs.docker.com/registry). Provides image hosting.
mkdir -p data && docker run --rm --interactive --tty --name takelship --hostname takelship --privileged --publish "35000:35000" --volume ./data:/home/podman/data takelwerk/takelship registry

== Project: forgejo
= Forgejo Gitea fork (forgejo.org). Provides git hosting. Provides CI/CD pipelines (GitHub style). Provides image hosting.
mkdir -p data && docker run --rm --interactive --tty --name takelship --hostname takelship --privileged --publish "30022:30022" --publish "33000:33000" --volume ./data:/home/podman/data takelwerk/takelship forgejo

== Project: teamcity
= TeamCity build server (jetbrains.com/teamcity). Provides CI/CD pipelines (JetBrains style). Runs with Forgejo for git hosting.
mkdir -p data && docker run --rm --interactive --tty --name takelship --hostname takelship --privileged --publish "30022:30022" --publish "33000:33000" --publish "38111:38111" --volume ./data:/home/podman/data takelwerk/takelship teamcity

== Project: update
= Update service files and run scripts in data directory.
mkdir -p data && docker run --rm --interactive --tty --volume ./data:/home/podman/data takelwerk/takelship update
```

List available container commands:

```bash
docker exec -it takelship cli
```

Run a command as podman user:

```bash
docker exec -it takelship cmd podman ps -a
```

Run a command as podman user in a different directory (`-w` or `--workdir`) than the default directory (`/home/podman`):

```bash
docker exec -it takelship cmd -w /tmp "podman info > ./podman_info"
docker exec -it takelship cmd cat /tmp/podman_info
```

Enter a login shell as podman user:

```bash
docker exec -it takelship cmd shell
```

Become root:

```bash
docker exec -it takelship bash
```
