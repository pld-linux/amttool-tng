Summary:	AmtTool TNG - utility to manage Intel AMT-aware devices
Summary(pl.UTF-8):	AmtTool TNG - narzędzie do zarządzania urządzeniami obsługującymi Intel AMT
Name:		amttool-tng
Version:	1.7
Release:	1
License:	GPL v2
Group:		Applications/Networking
# NOTE: keep versioned sf URLs here as file names are not versioned
Source0:	http://downloads.sourceforge.net/project/amttool-tng/%{version}/amttool
# Source0-md5:	e6b55df2a4f4912277103ab36249fe5d
Source1:	http://downloads.sourceforge.net/project/amttool-tng/%{version}/amt_traps_v1.4.sh
# Source1-md5:	222b81a003b8fd096f449d77d1d16614
Source2:	http://downloads.sourceforge.net/project/amttool-tng/%{version}/README.txt
# Source2-md5:	c012156e1ede183c7a154b0a4b6bd14d
URL:		http://amttool-tng.sourceforge.net/
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-SOAP-Lite
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This utility is further development of Gerd Hoffmann's AMTTOOL.

It now allows:
- remote power control with full sort of iAMT boot features
- view general, audit, remote device's info
- iAMT device network administration
- get/sync the iAMT device's time
- user access control management
- list hardware asset
- manipulation of Audit feature
- change various security settings
- manage iAMT power saving
- setup redirection service
- administer platform events logging
- alerting by SNMP traps.

%description -l pl.UTF-8
To narzędzie do dalszy rozwój narzędzia AMTTOOL Gerda Hoffmanna.

Obecnie umożliwia ono:
- zdalne sterowanie zasilaniem wraz ze wszystkimi rodzajami rozruchu
  iAMT
- oglądanie ogólnych, audytowych i zdalnych informacji o urządzeniu
- zarządzanie siecią urządzeń iAMT
- pobieranie i synchronizację czasu urządzeń iAMT
- zarządzanie listami kontroli dostępu użytkowników
- wypisywanie informacji o sprzęcie
- modyfikowanie opcji audytu
- zmianę różnych ustawień bezpieczeństwa
- zarządzanie oszczędzaniem energii iAMT
- usługę przekierowania konfiguracji
- administrowanie logowaniem zdarzeń platformy
- alarmowanie przy użyciu pułapek SNMP.

%prep
%setup -q -c -T

cp -p %{SOURCE1} amt_traps.sh
cp -p %{SOURCE2} .

%install
rm -rf $RPM_BUILD_ROOT

install -D %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}/amttool-tng

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt amt_traps.sh
%attr(755,root,root) %{_bindir}/amttool-tng
