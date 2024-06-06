Name:       lyrix
Version:    1
Release:    1
Summary:    display song lyrix in terminal
License:    GPLv3+
URL:        https://github.com/roguexsubmarine/Lyrix
Source0:    https://github.com/roguexsubmarine/Lyrix

Buildrequires:  make
Requires:       bash python python3

BuildArch:      noarch

%description
This is a command line application to scrape song lyrix from web

%build

%install
cp -rf lyrix_dist %{buildroot}/usr/bin/
cp lyrix %{buildroot}/usr/bin/	
chmod +x %{buildroot}/usr/bin/lyrix

%files
/usr/bin/lyrix
/usr/bin/lyrix/*

%changelog
* Thu June 06 2024 submarine <roguexsubmarine@gmail.com> - 1
- version 1

