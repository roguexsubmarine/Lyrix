Name:       lyrix
Version:    0.1.1
Release:    1
Summary:    display song lyrix in terminal
License:    GPLv3+
URL:        https://github.com/roguexsubmarine/Lyrix
Source0:    https://github.com/roguexsubmarine/Lyrix/release/%{name}-%{version}.tar.gz

Buildrequires:  make
Requires:       bash python python3
Requires:       python-requests
Requires:       python-bs4
Requires:       python-lxml

BuildArch:      noarch

%description
This is a command line application to scrape song lyrix from web

%prep
%setup -q

%build

%install
cp lyrix %{buildroot}/usr/bin/
chmod +x %{buildroot}/usr/bin/lyrix

%files

%changelog
* Mon Jun 10 2024 submarine <roguexsubmarine@gmail.com> - 0.1-1
- initial build

