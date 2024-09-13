---
id: dual-boot
aliases: []
tags: []
---

# Setting up dual boot **AFTER** linux

Have a live usb boot of linux to boot into, so you can edit partition size.
Using gparted to resize.

1. Create a partition for the windows installation

   - you may need to unmount the linux partition to unallocation some space
   - remount after resizing the partition

2. Boot into the windows installer and install windows onto the free/empty partition
3. reboot into linux and update grub to add windows to the boot loader
   - uncomment line 63 in `/etc/default/grub` `grub_disable_os_prober="false"`
     - update grub `sudo grub-mkconfig -o /boot/grub/grub.cfg`
   - on ubuntu use `sudo update-grub2`
