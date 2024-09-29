packer {
  required_plugins {
    ansible = {
      version = "~> 1"
      source = "github.com/hashicorp/ansible"
    }
    docker = {
      source  = "github.com/hashicorp/docker"
      version = "~> 1"
    }
  }
}

source "docker" "takelpodslim" {
  # export_path = "images/docker/${var.target_repo}.tar"
  image = "${var.base_user}/${var.base_repo}:${var.base_tag}"
  commit = true
  pull = false
  run_command = [
    "--detach",
    "--interactive",
    "--tty",
    "--privileged",
    "--name",
    "${var.target_repo}",
    "${var.base_user}/${var.base_repo}:${var.base_tag}",
    "/bin/bash"
  ]
  changes = [
    "WORKDIR /",
    "ENTRYPOINT [\"/entrypoint\"]",
    "ENV VERSION=${var.version}",
    "ENV DEBIAN_FRONTEND=noninteractive",
    "ENV LANG=C.UTF-8",
    "ENV SUPATH=$PATH",
    "ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
  ]
}

build {
  sources = [
    "source.docker.takelpodslim"
  ]

  provisioner "ansible" {
    extra_arguments = [
      "--extra-vars",
      "ansible_host=${var.target_repo} ansible_connection=docker"
    ]
    groups = [
      "all",
      "private",
      "users",
      "image",
      "${var.image_name}"
    ]
    playbook_file = "../ansible/${var.ansible_playbook}"
    user = "root"
  }

  post-processor "docker-tag" {
    repository = "${var.local_user}/${var.target_repo}"
    tags = ["${var.target_tag}"]
  }
}
