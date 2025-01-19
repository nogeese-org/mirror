# Nogeese Linux Mirror
A mirror with repos exclusive for Nogeese Linux, alongside the Arch Linux repos.

Nogeese Linux comes with it's repos.
## What are the repos?
nogeese - Official repo for Nogeese Linux programs.

bit - Handful utilities, you would normally not be able to install with pacman.
## How to get these repos on Arch Linux?
### nogeese
Even tho the nogeese repo was made for Nogeese Linux, you can still get it by editing the pacman config (/etc/pacman.conf):

Open "/etc/pacman.conf" in a text editor and

Add this line:

```
[nogeese]
Server = https://raw.githubusercontent.com/leon8326-nogeese/mirror/main/nogeese
SigLevel = TrustAll
```

### bit
The bit repo isn't made only for Nogeese Linux so you can just do the same:

Open "/etc/pacman.conf" in a text editor and

Add this line:

```
[bit]
Server = https://raw.githubusercontent.com/leon8326-nogeese/mirror/main/bit
SigLevel = TrustAll
```

### What about Nogeese AUR?
Check [the AUR's README](https://github.com/leon8326-nogeese/aur/README.md)


