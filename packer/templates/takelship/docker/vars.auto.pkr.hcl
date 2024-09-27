variable "image_name" {
  type = string
}

variable "ansible_playbook" {
  type = string
}

variable "base_repo" {
  type = string
}

variable "base_tag" {
  type = string
}

variable "base_user" {
  type = string
}

variable "local_user" {
  type = string
}

variable "mutagen" {
  type = string
  default = "invalid"
}

variable "target_repo" {
  type = string
}

variable "target_tag" {
  type = string
  default = "latest"
}

variable "version" {
  type = string
  default = "latest"
}

variable "packer_template_dir" {
  type = string
}
