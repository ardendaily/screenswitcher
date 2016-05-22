# screenswitcher

barebones, ncurses(ish?) frontend for managing screen sessions.

replace `screen ls && screen -R PIDOF.screen.session` with `screenswitcher`. great for arrow-key-dependent babies such as myself.

### install 

prerequisites thru pip:

    sudo pip install urwid

clone and drop this puppy in your path

    $ git clone https://github.com/ardendaily/screenswitcher.git
    $ cd screenswitcher
    $ cp screenswitcher.py ~/bin #maybe not necessary

**bonus** -- alias for lightning-fast screenswitchery. add to your .bashrc:

    alias rr='screenswitcher.py'
 
re-source your bashrc

    $ . .bashrc

now screenswitcher is almost on the homerow!

    $ rr

now you are cooking with fire!