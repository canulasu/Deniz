puts('------------------------------------------------------')
print('Deniz OS Dependency Installer Engine Version ')
print(RUBY_VERSION)
puts()
puts('------------------------------------------------------')

begin
    system("pip3 install colorama")
    system("pip install colorama")
    system("pip3 install psutil")
    system("pip install psutil")
    system("pip3 install PyQt5")
    system("pip install PyQt5")
    system("pip3 install PyQtWebEngine")
    system("pip install PyQtWebEngine")
    system("pip3 install wikipedia-api")
    system("pip install wikipedia-api")
end

puts('------------------------------------------------------')
puts('All Deniz Operating System Dependencies Installed')
