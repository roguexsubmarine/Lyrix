Name:       lyrix
Version:    1.0
Release:    1
Summary:    Display song lyrics in terminal
License:    GPLv3+
URL:        https://github.com/roguexsubmarine/Lyrix
Source0:    https://github.com/roguexsubmarine/Lyrix/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make

Requires:       bash python python3
Requires:       python-requests
Requires:       python-bs4
Requires:       python-lxml

BuildArch:      noarch

%description
This is a command line application to scrape song lyrics from the web.

%prep
%setup -q

%build
# Nothing to do here since not compiling anything

%install
install -Dm755 lyrix %{buildroot}%{_bindir}/lyrix

%files
%license LICENSE
%{_bindir}/lyrix

%changelog
* Mon Jun 10 2024 submarine <roguexsubmarine@gmail.com> - 1.0-1
- Initial build

