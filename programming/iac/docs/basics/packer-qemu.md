## Hello Packer

To convert the [Packer template](https://github.com/PacktPublishing/HashiCorp-Packer-in-Production/blob/main/Chapter02/hello.pkr.hcl) from using VirtualBox to QEMU, we'll need to change the source from `virtualbox-iso` to `qemu`. Note that the QEMU builder has different configuration options compared to VirtualBox, so we'll adjust those accordingly. Here's how the converted HCL2 Packer template might look:

```hcl
// HCL2 extrapolates builders as "sources"
source "qemu" "hello-base" {
  boot_command            = [
    "<esc><wait>", 
    "vmlinuz initrd=initrd.img ", 
    "inst.ks=https://github.com/jboero/hashistack/raw/master/http/ks-centosStreams.cfg", 
    "<enter>"
  ]
  boot_wait               = "3s"
  communicator            = "ssh"
  cpus                    = 2
  disk_size               = 100000
  disk_interface          = "virtio"
  format                  = "qcow2"
  headless                = false
  http_directory          = "http"
  iso_checksum            = "file:https://lon.mirror.rackspace.com/centos-stream/9-stream/BaseOS/x86_64/iso/CentOS-Stream-9-latest-x86_64-dvd1.iso.SHA256SUM"
  iso_url                 = "https://lon.mirror.rackspace.com/centos-stream/9-stream/BaseOS/x86_64/iso/CentOS-Stream-9-latest-x86_64-dvd1.iso"
  memory                  = 1024
  net_device              = "virtio-net"
  output_directory        = "output-qemu-hello-world"
  shutdown_command        = "shutdown -P now"
  ssh_username            = "root"
  ssh_password            = "packer"
  ssh_timeout             = "20m"
  vm_name                 = "hello-world.qcow2"
}

// Define a build with our single source builder and one provisioner.
build {
  sources = ["source.qemu.hello-base"]

  provisioner "file" {
    destination = "/etc/motd"
    direction   = "upload"
    source      = "./motd"
  }
}
```

### Key Changes and Considerations:

- **Builder Type**: Changed from `virtualbox-iso` to `qemu` to use QEMU for virtualization.
- **Disk Interface**: Specified as `virtio` for better performance with QEMU/KVM.
- **Format**: Changed to `qcow2`, a common disk image format used with QEMU.
- **Net Device**: Updated to `virtio-net` for network interface, aligning with QEMU's recommended settings.
- **Output Directory**: Adjusted to reflect QEMU output, specifying a directory where the output files will be placed.
- **VM Name**: The name of the output file now reflects the QEMU disk image format (`qcow2`).

Please adjust the `iso_checksum` and any specific boot commands or provisioning details according to your  requirements. The Kickstart file URL and any other configurations should be verified to ensure they are compatible with your target deployment environment and the CentOS Stream version you're using.

This example assumes you have a Kickstart configuration accessible at the specified URL and a local file named `motd` for the file provisioner. Adjust these to fit your setup.
