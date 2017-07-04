                                                                                            
      # ###                                         ##### ##  ###                           
    /  /###                                      ######  /###  ###                          
   /  /  ###                                    /#   /  /  ###  ##                          
  /  ##   ###                                  /    /  /    ### ##                          
 /  ###    ###                                     /  /      ## ##                          
##   ##     ##    /###     /##  ###  /###         ## ##      ## ##  ##   ####       /###    
##   ##     ##   / ###  / / ###  ###/ #### /      ## ##      ## ##   ##    ###  /  / #### / 
##   ##     ##  /   ###/ /   ###  ##   ###/     /### ##      /  ##   ##     ###/  ##  ###/  
##   ##     ## ##    ## ##    ### ##    ##     / ### ##     /   ##   ##      ##  ####       
##   ##     ## ##    ## ########  ##    ##        ## ######/    ##   ##      ##    ###      
 ##  ##     ## ##    ## #######   ##    ##        ## ######     ##   ##      ##      ###    
  ## #      /  ##    ## ##        ##    ##        ## ##         ##   ##      ##        ###  
   ###     /   ##    ## ####    / ##    ##        ## ##         ##   ##      /#   /###  ##  
    ######/    #######   ######/  ###   ###       ## ##         ### / ######/ ## / #### /   
      ###      ######     #####    ###   ### ##   ## ##          ##/   #####   ##   ###/    
               ##                           ###   #  /                              

## Our buildserver is currently running on: ##

Debian Jessie (GNU/Linux 2.6.32-37-pve)
=======

## OpenPlus 2.0 is build using oe-alliance build-environment and several git repositories: ##

> [https://github.com/oe-alliance/oe-alliance-core/tree/3.4](https://github.com/oe-alliance/oe-alliance-core/tree/3.4 "OE-Alliance")
> 
> [https://github.com/open-plus/enigma](https://github.com/open-plus/enigma "OpenPlus E2")

> and a lot more...


----------

# Building Instructions #

1 - Install packages on your buildserver

    sudo apt-get install -y autoconf automake bison bzip2 cvs diffstat flex g++ gawk gcc gettext git-core gzip help2man ncurses-bin ncurses-dev libc6-dev libtool make texinfo patch perl pkg-config subversion tar texi2html wget zlib1g-dev chrpath libxml2-utils xsltproc libglib2.0-dev python-setuptools zip info coreutils diffstat chrpath libproc-processtable-perl libperl4-corelibs-perl sshpass default-jre default-jre-headless java-common  libserf-dev
----------
2 - Set your shell to /bin/bash.

    sudo dpkg-reconfigure dash
    When asked: Install dash as /bin/sh?
    select "NO"

----------
3 - Add user openplusbuilder

    sudo adduser openplusbuilder

----------
4 - Switch to user openplusbuilder

    su openplusbuilder

----------
5 - Switch to home of openplusbuilder

    cd ~

----------
6 - Create folder openplus

    mkdir -p ~/openplus

----------
7 - Switch to folder openplus

    cd openplus

----------
8 - Clone oe-alliance git

    git clone git://github.com/oe-alliance/build-enviroment.git -b 3.4

----------
9 - Switch to folder build-enviroment

    cd build-enviroment

----------
10 - Update build-enviroment

    make update

----------
11 - Finally you can start building a image

    MACHINE=gbquadplus DISTRO=openplus make image
