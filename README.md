# Nogeese Linux Mirror
A mirror with repos exclusive for Nogeese Linux, alongside the Arch Linux repos.

Nogeese Linux comes with it's repos.
## What are the repos?
nogeese - Official repo for Nogeese Linux programs.

bit - Handful utilities, you would normally not be able to install with pacman.
## How to get these repos on Arch Linux?
### nogeese
Even tho the nogeese repo was made for Nogeese Linux, you can still get it by editing the pacman config (/etc/pacman.conf):

Before adding ANY repo run:

```
echo "arch=(ARCHITECTURE HERE)" >> ~/.bashrc
source ~/.bashrc
```

Open "/etc/pacman.conf" in a text editor and

Add this line:

```
[nogeese]
Server = https://raw.githubusercontent.com/leon8326-nogeese/mirror/main/nogeese/os/$arch
SigLevel = Optional TrustAll
```

### bit
The bit repo isn't made only for Nogeese Linux so you can just do the same:

Open "/etc/pacman.conf" in a text editor and

Add this line:

```
[bit]
Server = https://raw.githubusercontent.com/leon8326-nogeese/mirror/main/bit/os/$arch
SigLevel = Optional TrustAll
```

### What about Nogeese AUR?
Check [the AUR's README](https://github.com/leon8326-nogeese/aur/blob/main/README.md).

## As a developer, how can i upload a new package on this mirror?
PLEASE Read which repo your package should be in the "What are the repos?" section of this README.

If your package doesn't fit to any of the repos, consider using the Nogeese AUR.

Fork this mirror, and download the .db and .files on the repo ($repo/os/$arch) you want to have your package on, for this example we will add yay to the bit repo.

In this example that would be bit/os/x86_64.

Make sure it is a separate new directory with all the .db and .files in it.

Now add the *.pkg.tar or *.pkg.tar.zst package onto the same directory.

In this example it will be yay-*-x86_64.pkg.tar.zst.

Paste this package into the same directory as all the .db and .files.

Then run this command in the same directory:

```
repo-add $repo.db.tar.gz $package-*-$arch(.pkg.tar/.pkg.tar.zst)
```

In this example it will be:

```
repo-add bit.db.tar.gz yay-*-x86_64.pkg.tar.zst
```

And then delete ALL the .db and .files in the repo directory on the fork you created on github.

And in the same directory click + > Upload files and drag and drop the .pkg.tar/.pkg.tar.zst and all the .db and .files, then click "Commit changes".

Go to the home page of the fork and click "Contribute" follow instrustion on the screen, and wait... your package should be approved. 

## What are the architectures and what are they based on?

x86_64 - Based on [Arch Linux](https://archlinux.org)

x86 - Based on [Arch Linux 32](https://archlinux32.org)

aarch64 & arm - Based on [Arch Linux ARM](https://archlinuxarm.org)

powerpc & powerpc64 - Based on [ArchPOWER](https://archlinuxpower.org)

risc-v - Based on [Arch Linux RISC-V](https://archriscv.felixc.at/)
