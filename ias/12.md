To conduct a simple experiment using Packer to create an image and then testing it on QEMU on an Ubuntu 22.04 system, follow these step-by-step instructions. This experiment will create a basic Ubuntu server image and then run it with QEMU.

### Step 1: Install Required Software

First, ensure you have Packer and QEMU installed on your Ubuntu 22.04 system. Open a terminal and run:

```bash
sudo apt update
sudo apt install -y packer qemu qemu-kvm
```

### Step 2: Prepare Packer Template

Create a directory for your Packer project and navigate into it:

```bash
mkdir ~/packer-qemu-experiment
cd ~/packer-qemu-experiment
```

Create a Packer template file named `ubuntu.json` with the following content. This defines a simple Packer build configuration for creating an Ubuntu server image. Replace `"iso_url"` and `"iso_checksum"` with the appropriate URL and checksum for the Ubuntu server ISO you want to use.

```json
{
  "builders": [
    {
      "type": "qemu",
      "iso_url": "http://releases.ubuntu.com/22.04/ubuntu-22.04-live-server-amd64.iso",
      "iso_checksum": "sha256:9b3f83e09f0a6e3f74c0f9e4e6d2e6f0e0c9c4f2c9a6e5c05f6c0059d6c2a3ee",
      "disk_size": 10240,
      "format": "qcow2",
      "accelerator": "kvm",
      "net_device": "user",
      "memory": 2048,
      "cpus": 2,
      "ssh_username": "ubuntu",
      "ssh_password": "ubuntu",
      "ssh_timeout": "30m",
      "boot_wait": "10s",
      "boot_command": [
        "<enter><wait>",
        "sudo -s<enter><wait>",
        "echo 'ubuntu:ubuntu' | chpasswd<enter><wait>",
        "apt-get update<enter><wait>",
        "apt-get install -y openssh-server<enter><wait>",
        "<wait10>",
        "systemctl start ssh<enter><wait>",
        "<wait10>",
        "echo 'Done.'<enter>"
      ]
    }
  ],
  "provisioners": [
    {
      "type": "shell",
      "inline": ["echo 'Packer Build Complete'"]
    }
  ]
}
```

**Note**: This template is a simplified example for demonstration purposes. The boot command sequence might need adjustments based on the specific ISO's installation process.

### Step 3: Build the Image with Packer

Run Packer to create your image:

```bash
packer build ubuntu.json
```

Packer will download the Ubuntu ISO, create a VM, and execute the specified boot commands to install Ubuntu and configure it. After completion, you'll have a `.qcow2` image ready for use with QEMU.

### Step 4: Run the Image with QEMU

After the build process completes, start the VM using QEMU with the generated QCOW2 image file. The image file will be named as `packer-qemu` followed by a timestamp. Adjust the file name in the command below as necessary:

```bash
qemu-system-x86_64 -m 2048 -smp cpus=2 -hda output-qemu/packer-qemu-<timestamp>.qcow2 -accel kvm -net nic -net user
```

This command starts the virtual machine with 2048 MB of RAM and 2 CPUs, using the image you created. You'll see the VM boot up in a new window.

### Step 5: Testing and Experimentation

Now that your VM is running, you can connect to it using SSH (if you've set up networking and SSH access correctly) or interact with it directly through the QEMU window. This setup allows you to test the image, deploy applications, and experiment with configurations.

### Conclusion

This experiment demonstrates a simple workflow for creating and testing a virtual machine image using Packer and QEMU. You can expand upon this foundation by customizing the Packer template with more complex provisioning scripts, experimenting with different operating systems, or exploring advanced QEMU options for networking and performance.
