# salt-init

This tool is for simple server management with [Salt Stack](http://www.saltstack.com/).

What it does is:
 * Bootstraps Salt Stack (via [salt-bootstrap](https://github.com/saltstack/salt-bootstrap/))
 * Allows you to merge multiple Salt state trees
 * Auto-generates a combined top.sls for the merged trees (`*` sections only)
 * Runs salt on your server


## Usage

*Step 1:*
Fork this repository.

*Step 2:*
Edit the files under default/ with any and all "default" states you want 
applied on all of your servers.

*Step 3:*
Add git submodules 
([git submodule add](http://git-scm.com/book/en/v2/Git-Tools-Submodules)) for 
other Salt state trees you might want merged on some of your servers.

*Step 4:*
Check out your repository on the target server, with the submodules:
```
git clone --recursive https://github.com/your-name/your-fork.git
# Or on older versions of git
git clone https://github.com/your-name/your-fork.git
cd your-fork
git submodule update --init --recursive
```

*Step 5:*
Run initialize.sh, you can give it the paths of the extra salt states 
trees (directories containing top.sls). The "default" tree will always be applied:
```
cd your-fork
./initialize.sh
# Or:
./initialize.sh submoduleA/salt submoduleB/foo/bar/salt/
```
