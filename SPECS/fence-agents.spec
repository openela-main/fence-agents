###############################################################################
###############################################################################
##
##  Copyright (C) 2019-2021 Red Hat, Inc.  All rights reserved.
##
##  This copyrighted material is made available to anyone wishing to use,
##  modify, copy, or redistribute it subject to the terms and conditions
##  of the GNU General Public License v.2.
##
###############################################################################
###############################################################################

Name: fence-agents
Summary: Set of unified programs capable of host isolation ("fencing")
Version: 4.16.0
Release: 5%{?alphatag:.%{alphatag}}%{?dist}.5
License: GPL-2.0-or-later AND LGPL-2.0-or-later
URL: https://github.com/ClusterLabs/fence-agents
Source0: https://fedorahosted.org/releases/f/e/fence-agents/%{name}-%{version}.tar.gz
### HA support requirements-*.txt ###
Source100: requirements-common.txt
Source101: requirements-aliyun.txt
Source102: requirements-aws.txt
Source103: requirements-azure.txt
Source104: requirements-google.txt
### HA support libs/utils ###
### BEGIN ###
## pip download --no-binary :all: -r requirements-<name>.txt
# common
Source1000: pycurl-7.45.3.tar.gz
Source1001: suds-community-1.1.2.tar.gz
# aliyun
Source1100: aliyun-python-sdk-ecs-4.24.71.tar.gz
Source1101: aliyun-python-sdk-core-2.14.0.tar.gz
Source1102: jmespath-0.10.0.tar.gz
# aliyun-cli
Source1150: aliyun-cli-3.0.198.tar.gz
## TAG=$(git log --pretty="format:%h" -n 1)
## distdir="aliyun-openapi-meta-${TAG}"
## TARFILE="${distdir}.tar.gz"
## rm -rf $TARFILE $distdir
## git archive --prefix=$distdir/ HEAD | gzip > $TARFILE
Source1151: aliyun-openapi-meta-5cf98b660.tar.gz
## go mod vendor
Source1152: aliyun-cli-go-vendor.tar.gz
# aws
Source1200: boto3-1.40.13.tar.gz
Source1201: botocore-1.40.13.tar.gz
Source1202: s3transfer-0.13.1.tar.gz
# azure
Source1300: azure-common-1.1.28.zip
Source1301: azure_core-1.32.0.tar.gz
Source1302: azure_mgmt_core-1.5.0.tar.gz
Source1303: azure_mgmt_compute-34.0.0.tar.gz
Source1304: azure_mgmt_network-28.1.0.tar.gz
Source1305: azure_identity-1.19.0.tar.gz
Source1306: msal-1.31.1.tar.gz
Source1307: msal_extensions-1.2.0.tar.gz
Source1308: msrest-0.7.1.zip
Source1309: msrestazure-0.6.4.post1.tar.gz
Source1310: adal-1.2.7.tar.gz
Source1311: certifi-2025.1.31.tar.gz
Source1312: isodate-0.6.1.tar.gz
Source1313: portalocker-2.10.1.tar.gz
Source1314: pyjwt-2.10.1.tar.gz
# google
Source1400: google-api-python-client-1.12.8.tar.gz
Source1401: chardet-3.0.4.tar.gz
Source1402: google-api-core-1.34.1.tar.gz
Source1403: google-auth-2.28.1.tar.gz
Source1404: google-auth-httplib2-0.2.0.tar.gz
Source1405: httplib2-0.22.0.tar.gz
Source1406: uritemplate-3.0.1.tar.gz
Source1407: cachetools-5.3.2.tar.gz
Source1408: googleapis-common-protos-1.62.0.tar.gz
Source1409: pyasn1-0.5.1.tar.gz
Source1410: pyasn1_modules-0.3.0.tar.gz
Source1411: pyroute2-0.7.12.tar.gz
Source1412: pyroute2.core-0.6.13.tar.gz
Source1413: pyroute2.ethtool-0.6.13.tar.gz
Source1414: pyroute2.ipdb-0.6.13.tar.gz
Source1415: pyroute2.ipset-0.6.13.tar.gz
Source1416: pyroute2.ndb-0.6.13.tar.gz
Source1417: pyroute2.nftables-0.6.13.tar.gz
Source1418: pyroute2.nslink-0.6.13.tar.gz
## NEEEDED FOR GOOGLE AUTH
## INFO: pip is looking at multiple versions of google-auth to determine which version is compatible with other requirements. This could take a while.
## ERROR: Could not find a version that satisfies the requirement rsa<5,>=3.1.4 (from google-auth) (from versions: none)
Source1518: rsa-4.9.tar.gz
# google buildreq
Source1519: poetry_core-1.9.0.tar.gz
# kubevirt
## pip download --no-binary :all: openshift
Source1600: openshift-0.13.2.tar.gz
Source1601: kubernetes-29.0.0.tar.gz
Source1602: python-string-utils-1.0.0.tar.gz
Source1603: websocket-client-1.7.0.tar.gz
### END

Patch0: build-pythonpath.patch
Patch1: RHEL-76495-fence_azure_arm-use-azure-identity.patch
Patch2: ha-cloud-support-aliyun.patch
Patch3: ha-cloud-support-aws.patch
Patch4: ha-cloud-support-azure.patch
Patch5: ha-cloud-support-google.patch
Patch6: bundled-kubevirt.patch
Patch7: bundled-pycurl.patch
Patch8: bundled-suds.patch
Patch9: RHEL-83774-fence_ibm_vpc-refresh-bearer-token.patch
Patch10: RHEL-107530-fence_ibm_vpc-add-apikey-file-support.patch
Patch11: RHEL-109922-fence_aws-add-skipshutdown-parameter.patch

%global supportedagents amt_ws apc apc_snmp bladecenter brocade cisco_mds cisco_ucs drac5 eaton_snmp emerson eps hpblade ibmblade ibm_powervs ibm_vpc ifmib ilo ilo_moonshot ilo_mp ilo_ssh intelmodular ipdu ipmilan kdump kubevirt lpar mpath redfish rhevm rsa rsb sbd scsi vmware_rest vmware_soap wti
%ifarch x86_64
%global testagents virsh heuristics_ping aliyun aws azure_arm gce openstack virt
%endif
%ifarch ppc64le
%global testagents virsh heuristics_ping openstack
%endif
%ifarch s390x
%global testagents virsh zvm heuristics_ping
%endif
%ifnarch x86_64 ppc64le s390x
%global testagents virsh heuristics_ping
%endif

# skipped: pve, raritan, rcd-serial, virsh
%global allfenceagents %(cat <<EOF
fence-agents-amt-ws \\
fence-agents-apc \\
fence-agents-apc-snmp \\
fence-agents-bladecenter \\
fence-agents-brocade \\
fence-agents-cisco-mds \\
fence-agents-cisco-ucs \\
fence-agents-drac5 \\
fence-agents-eaton-snmp \\
fence-agents-emerson \\
fence-agents-eps \\
fence-agents-heuristics-ping \\
fence-agents-hpblade \\
fence-agents-ibmblade \\
fence-agents-ifmib \\
fence-agents-ilo-moonshot \\
fence-agents-ilo-mp \\
fence-agents-ilo-ssh \\
fence-agents-ilo2 \\
fence-agents-intelmodular \\
fence-agents-ipdu \\
fence-agents-ipmilan \\
fence-agents-kdump \\
fence-agents-mpath \\
fence-agents-redfish \\
fence-agents-rhevm \\
fence-agents-rsa \\
fence-agents-rsb \\
fence-agents-sbd \\
fence-agents-scsi \\
fence-agents-vmware-rest \\
fence-agents-vmware-soap \\
fence-agents-wti \\

EOF)

%ifarch x86_64
%global allfenceagents %(cat <<EOF
%{allfenceagents} \\
fence-virt \\

EOF)
%endif

# Build dependencies
## general
BuildRequires: autoconf automake libtool make
## compiled code (-kdump)
BuildRequires: gcc
## man pages generating
BuildRequires: libxslt
## Python dependencies
BuildRequires: python3-devel
# dependencies for building HA support subpackages
BuildRequires: python3-pip python3-wheel python3-setuptools libcurl-devel git openssl-devel
%ifarch x86_64
BuildRequires: golang go-rpm-macros
%endif
# dependencies for HA support subpackages
BuildRequires: python3-pexpect python3-ptyprocess python3-colorama python3-docutils python3-pyyaml python3-jmespath python3-pyasn1 python3-dateutil python3-urllib3 python3-six python3-cryptography python3-cffi python3-requests python3-requests-oauthlib python3-typing-extensions python3-packaging python3-charset-normalizer python3-idna python3-oauthlib python3-pycparser python3-protobuf python3-pyparsing

%if 0%{?fedora} || 0%{?centos} || 0%{?rhel}
BuildRequires: openwsman-python3
%else
BuildRequires: python3-openwsman
%endif

# fence-virt
%if 0%{?suse_version}
%define nss_devel mozilla-nss-devel
%define nspr_devel mozilla-nspr-devel
%define systemd_units systemd
%else
%define nss_devel nss-devel
%define nspr_devel nspr-devel
%define systemd_units systemd-units
%endif

BuildRequires:  corosynclib-devel libvirt-devel
BuildRequires:  libxml2-devel %{nss_devel} %{nspr_devel}
BuildRequires:  flex bison libuuid-devel
BuildRequires: %{systemd_units}


# turn off the brp-python-bytecompile script
# (for F28+ or equivalent, the latter is the preferred form)
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompilespace:.*$!!g')
#undefine __brp_python_bytecompile

%prep
%setup -q -n %{name}-%{version}%{?rcver:%{rcver}}%{?numcomm:.%{numcomm}}%{?alphatag:-%{alphatag}}%{?dirty:-%{dirty}}
%patch -p1 -P 0
%patch -p1 -P 1
%patch -p1 -P 2
%patch -p1 -P 3
%patch -p1 -P 4
%patch -p1 -P 5
%patch -p1 -P 6
%patch -p1 -P 7
%patch -p1 -P 8
%patch -p1 -P 9
%patch -p1 -P 10
%patch -p1 -P 11 -F2

# prevent compilation of something that won't get used anyway
sed -i.orig 's|FENCE_ZVM=1|FENCE_ZVM=0|' configure.ac

%build
export PYTHON="%{__python3}"

# aliyun-cli
%ifarch x86_64
tar zxf %SOURCE1150
pushd aliyun-cli-*
git init
rmdir aliyun-openapi-meta
tar zxf %SOURCE1151
tar zxf %SOURCE1152
mv aliyun-openapi-meta-* aliyun-openapi-meta
TMPLDFLAGS="$LDFLAGS"
%define aliyun_cli_version 3.0.198
export LDFLAGS="-X github.com/aliyun/aliyun-cli/cli.Version=%{aliyun_cli_version}"
go build %{gobuildflags} -mod=vendor -o out/aliyun main/main.go
export LDFLAGS="$TMPLDFLAGS"
unset TMPLDFLAGS
mkdir -p ../support/aliyun/aliyun-cli
install -m 0755 out/aliyun ../support/aliyun/aliyun-cli/
popd
%endif

# support libs
%{__python3} -m pip install --no-build-isolation --user --no-index --find-links %{_sourcedir} poetry-core

%ifarch x86_64
LIBS="%{_sourcedir}/requirements-*.txt"
%endif
%ifnarch x86_64
LIBS="%{_sourcedir}/requirements-common.txt"
%endif
for x in $LIBS; do
	%{__python3} -m pip install --no-build-isolation --prefix "" --root support/$(echo $x | sed -E "s/.*requirements-(.*).txt/\1/") --no-index --find-links %{_sourcedir} -r $x
done

# kubevirt
%{__python3} -m pip install --no-build-isolation --prefix "" --root support/kubevirt --no-index --find-links %{_sourcedir} openshift suds-community
rm -rf kubevirt/rsa*

for dir in support/*; do
	rm -rf $dir/bin
done

# avoid buildtime errors
%{__python3} -m pip install --no-build-isolation --user --no-index --find-links %{_sourcedir} suds-community

sed -i -e "s/#PYTHON3_VERSION#/%{python3_version}/" lib/*.py agents/*/*.py

export PYTHONPATH="%{_builddir}/%{name}-%{version}/support/common/lib/python%{python3_version}/site-packages:%{_builddir}/%{name}-%{version}/support/common/lib64/python%{python3_version}/site-packages:%{_builddir}/%{name}-%{version}/support/aliyun/lib/python%{python3_version}/site-packages:%{_builddir}/%{name}-%{version}/support/aws/lib/python%{python3_version}/site-packages:%{_builddir}/%{name}-%{version}/support/azure/lib/python%{python3_version}/site-packages:%{_builddir}/%{name}-%{version}/support/google/lib/python%{python3_version}/site-packages:%{_builddir}/%{name}-%{version}/support/kubevirt/lib/python%{python3_version}/site-packages:%{_builddir}/%{name}-%{version}/support/kubevirt/lib64/python%{python3_version}/site-packages"
./autogen.sh
%{configure} \
%if %{defined _tmpfilesdir}
	SYSTEMD_TMPFILES_DIR=%{_tmpfilesdir} \
	--with-fencetmpdir=/run/fence-agents \
%endif
	--with-agents='%{supportedagents} %{testagents}'

CFLAGS="$(echo '%{optflags}')" make %{_smp_mflags}

%install
rm -rf %{buildroot}

# support libs
mkdir -p %{buildroot}%{_usr}/lib/%{name}
mv support %{buildroot}%{_usr}/lib/%{name}

export PYTHONPATH="%{buildroot}%{_usr}/lib/%{name}/support/common/lib/python%{python3_version}/site-packages:%{buildroot}%{_usr}/lib/%{name}/support/common/lib64/python%{python3_version}/site-packages:%{buildroot}%{_usr}/lib/%{name}/support/aliyun/lib/python%{python3_version}/site-packages:%{buildroot}%{_usr}/lib/%{name}/support/aws/lib/python%{python3_version}/site-packages:%{buildroot}%{_usr}/lib/%{name}/support/azure/lib/python%{python3_version}/site-packages:%{buildroot}%{_usr}/lib/%{name}/support/google/lib/python%{python3_version}/site-packages:%{buildroot}%{_usr}/lib/%{name}/support/kubevirt/lib/python%{python3_version}/site-packages:%{buildroot}%{_usr}/lib/%{name}/support/kubevirt/lib64/python%{python3_version}/site-packages"
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}/%{_unitdir}/
%ifarch x86_64
install -m 0644 agents/virt/fence_virtd.service %{buildroot}/%{_unitdir}/
%endif
# bytecompile Python source code in a non-standard location
%if 0%{?fedora} || 0%{?centos} || 0%{?rhel}
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/fence
%endif
# XXX unsure if /usr/sbin/fence_* should be compiled as well

## tree fix up
# fix libfence permissions
chmod 0755 %{buildroot}%{_datadir}/fence/*.py
# remove docs
rm -rf %{buildroot}/usr/share/doc/fence-agents
# remove .a files
rm -f %{buildroot}/%{_libdir}/%{name}/*.*a
rm -f %{buildroot}/%{_libdir}/fence-virt/*.*a

%post
ccs_update_schema > /dev/null 2>&1 ||:
# https://fedoraproject.org/wiki/Packaging:ScriptletSnippets#Systemd
if [ $1 -eq 1 ] ; then
    # Initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%preun
# https://fedoraproject.org/wiki/Packaging:ScriptletSnippets#Systemd
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable fence_virtd.service &> /dev/null || :
    /bin/systemctl stop fence_virtd.service &> /dev/null || :
fi

%postun
# https://fedoraproject.org/wiki/Packaging:ScriptletSnippets#Systemd
/bin/systemctl daemon-reload &> /dev/null || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart fence_virtd.service &> /dev/null || :
fi

%triggerun -- fence_virtd < 0.3.0-1
# https://fedoraproject.org/wiki/Packaging:ScriptletSnippets#Packages_migrating_to_a_systemd_unit_file_from_a_SysV_initscript
/usr/bin/systemd-sysv-convert --save fence_virtd &> /dev/null || :
/sbin/chkconfig --del fence_virtd &> /dev/null || :
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
/bin/systemctl try-restart fence_virtd.service &> /dev/null || :

%description
A collection of executables to handle isolation ("fencing") of possibly
misbehaving hosts by the means of remote power management, blocking
network, storage, or similar. They operate through a unified interface
(calling conventions) devised for the original Red Hat clustering solution.

%package common
License: GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-3.0-or-later AND LGPL-2.1-or-later AND MIT
Summary: Common base for Fence Agents
Requires: python3-pexpect python3-ptyprocess
Provides: bundled(python3-pycurl) = 7.45.3
Provides: bundled(python3-suds-community) = 1.1.2
%description common
A collection of executables to handle isolation ("fencing") of possibly
misbehaving hosts by the means of remote power management, blocking
network, storage, or similar.

This package contains support files including the Python fencing library.
%files common
%doc doc/COPYING.* doc/COPYRIGHT doc/README.licence
%{_datadir}/fence
%exclude %{_datadir}/fence/azure_fence.*
%exclude %{_datadir}/fence/__pycache__/azure_fence.*
%{_datadir}/cluster
%exclude %{_datadir}/cluster/fence_mpath_check*
%exclude %{_datadir}/cluster/fence_scsi_check*
%{_datadir}/pkgconfig/%{name}.pc
%exclude %{_sbindir}/*
%exclude %{_mandir}/man8/*
%if %{defined _tmpfilesdir}
%{_tmpfilesdir}/%{name}.conf
%endif
%if %{defined _tmpfilesdir}
%dir %attr (1755, root, root)	/run/%{name}
%else
%dir %attr (1755, root, root)	%{_var}/run/%{name}
%endif
%dir %{_usr}/lib/%{name}
%{_usr}/lib/%{name}/support/common/lib*
%exclude %{_usr}/lib/%{name}/support/common/share

%ifarch x86_64
%package -n ha-cloud-support
License: GPL-2.0-or-later AND LGPL-2.0-or-later AND Apache-2.0 AND MIT AND BSD-2-Clause AND BSD-3-Clause AND MPL-2.0 AND LGPL-2.1-or-later AND ISC
Summary: Support libraries for HA Cloud agents
Requires: python3-colorama python3-docutils python3-pyyaml python3-jmespath python3-pyasn1 python3-dateutil python3-urllib3 python3-six python3-cryptography python3-cffi python3-requests python3-requests-oauthlib python3-typing-extensions python3-packaging python3-charset-normalizer python3-idna python3-oauthlib python3-pycparser python3-protobuf python3-pyparsing
Requires: awscli2
# aliyun
Provides: bundled(python3-aliyun-python-sdk-ecs) = 4.24.71
Provides: bundled(python3-aliyun-python-sdk-core) = 2.14.0
Provides: bundled(python3-jmespath) = 0.10.0
Provides: bundled(aliyun-cli) = 3.0.198
Provides: bundled(aliyun-openapi-meta) = 5cf98b660
# aws
Provides: bundled(python3-boto3) = 1.40.13
Provides: bundled(python3-botocore) = 1.40.13
Provides: bundled(python3-s3transfer) = 0.13.1
# azure
Provides: bundled(python3-azure-common) = 1.1.28
Provides: bundled(python3-azure-core) = 1.32.0
Provides: bundled(python3-azure-mgmt-core) = 1.5.0
Provides: bundled(python3-azure-mgmt-compute) = 34.0.0
Provides: bundled(python3-azure-mgmt-network) = 28.1.0
Provides: bundled(python3-azure-identity) = 1.19.0
Provides: bundled(python3-msal) = 1.31.1
Provides: bundled(python3-msal-extensions) = 1.2.0
Provides: bundled(python3-msrest) = 0.7.1
Provides: bundled(python3-msrestazure) = 0.6.4.post1
Provides: bundled(python3-adal) = 1.2.7
Provides: bundled(python3-certifi) = 2025.1.31
Provides: bundled(python3-isodate) = 0.6.1
Provides: bundled(python3-portalocker) = 2.10.1
Provides: bundled(python3-PyJWT) = 2.10.1
# google
Provides: bundled(python3-google-api-python-client) = 1.12.8
Provides: bundled(python3-chardet) = 3.0.4
Provides: bundled(python3-google-api-core) = 1.34.1
Provides: bundled(python3-google-auth) = 2.28.1
Provides: bundled(python3-google-auth-httplib2) = 0.2.0
Provides: bundled(python3-httplib2) = 0.22.0
Provides: bundled(python3-uritemplate) = 3.0.1
Provides: bundled(python3-cachetools) = 5.3.2
Provides: bundled(python3-googleapis-common-protos) = 1.62.0
Provides: bundled(python3-pyasn1) = 0.5.1
Provides: bundled(python3-pyasn1_modules) = 0.3.0
Provides: bundled(python-pyroute2) = 0.7.12
Provides: bundled(python-pyroute2-core) = 0.6.13
Provides: bundled(python-pyroute2-ethtool) = 0.6.13
Provides: bundled(python-pyroute2-ipdb) = 0.6.13
Provides: bundled(python-pyroute2-ipset) = 0.6.13
Provides: bundled(python-pyroute2-ndb) = 0.6.13
Provides: bundled(python-pyroute2-nftables) = 0.6.13
Provides: bundled(python-pyroute2-nslink) = 0.6.13
Provides: bundled(python3-rsa) = 4.9
%description -n ha-cloud-support
Support libraries for Fence Agents.
%files -n ha-cloud-support
%dir %{_usr}/lib/%{name}
%{_usr}/lib/%{name}/support/*/lib
%{_usr}/lib/%{name}/support/aliyun/aliyun-cli
%exclude %{_usr}/lib/%{name}/support/common
%exclude %{_usr}/lib/%{name}/support/kubevirt
%endif

%package all
License: GPL-2.0-or-later AND LGPL-2.0-or-later AND Apache-2.0
Summary: Set of unified programs capable of host isolation ("fencing")
Requires: %{allfenceagents}
%ifarch ppc64le
Requires: fence-agents-lpar >= %{version}-%{release}
%endif
%ifarch s390x
Requires: fence-agents-zvm >= %{version}-%{release}
%endif
Provides: fence-agents = %{version}-%{release}
Obsoletes: fence-agents < 3.1.13
%description all
A collection of executables to handle isolation ("fencing") of possibly
misbehaving hosts by the means of remote power management, blocking
network, storage, or similar.

This package serves as a catch-all for all supported fence agents.
%files all

%ifarch x86_64
%package aliyun
License: GPL-2.0-or-later AND LGPL-2.0-or-later AND Apache-2.0 AND BSD-3-Clause AND MIT
Group: System Environment/Base
Summary: Fence agent for Alibaba Cloud (Aliyun)
Requires: fence-agents-common >= %{version}-%{release}
Requires: ha-cloud-support = %{version}-%{release}
Requires: python3-jmespath >= 0.9.0
Obsoletes: %{name} < %{version}-%{release}
%description aliyun
The fence-agents-aliyun package contains a fence agent for Alibaba Cloud (Aliyun) instances.
%files aliyun
%defattr(-,root,root,-)
%{_sbindir}/fence_aliyun
%{_mandir}/man8/fence_aliyun.8*
%endif

%package amt-ws
License: Apache-2.0
Summary: Fence agent for Intel AMT (WS-Man) devices
Requires: fence-agents-common = %{version}-%{release}
%if 0%{?fedora} || 0%{?centos} || 0%{?rhel}
Requires: openwsman-python3
%else
Requires: python3-openwsman
%endif
BuildArch: noarch
%description amt-ws
Fence agent for AMT (WS-Man) devices.
%files amt-ws
%{_sbindir}/fence_amt_ws
%{_mandir}/man8/fence_amt_ws.8*

%package apc
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for APC devices
Requires: openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
Recommends: telnet
%endif
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description apc
Fence agent for APC devices that are accessed via telnet or SSH.
%files apc
%{_sbindir}/fence_apc
%{_mandir}/man8/fence_apc.8*

%package apc-snmp
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agents for APC devices (SNMP)
Requires: net-snmp-utils
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description apc-snmp
Fence agents for APC devices that are accessed via the SNMP protocol.
%files apc-snmp
%{_sbindir}/fence_apc_snmp
%{_mandir}/man8/fence_apc_snmp.8*
%{_sbindir}/fence_tripplite_snmp
%{_mandir}/man8/fence_tripplite_snmp.8*

%ifarch x86_64
%package aws
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for Amazon AWS
Requires: fence-agents-common = %{version}-%{release}
Requires: ha-cloud-support = %{version}-%{release}
Obsoletes: fence-agents < 3.1.13
%description aws
Fence agent for Amazon AWS instances.
%files aws
%{_sbindir}/fence_aws
%{_mandir}/man8/fence_aws.8*
%endif

%ifarch x86_64
%package azure-arm
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for Azure Resource Manager
Requires: fence-agents-common = %{version}-%{release}
Requires: ha-cloud-support = %{version}-%{release}
Obsoletes: fence-agents < 3.1.13
%description azure-arm
Fence agent for Azure Resource Manager instances.
%files azure-arm
%{_sbindir}/fence_azure_arm
%{_datadir}/fence/azure_fence.py*
%if 0%{?fedora} || 0%{?centos} || 0%{?rhel}
%{_datadir}/fence/__pycache__/azure_fence.*
%endif
%{_mandir}/man8/fence_azure_arm.8*
%endif

%package bladecenter
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for IBM BladeCenter
Requires: openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
Recommends: telnet
%endif
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description bladecenter
Fence agent for IBM BladeCenter devices that are accessed
via telnet or SSH.
%files bladecenter
%{_sbindir}/fence_bladecenter
%{_mandir}/man8/fence_bladecenter.8*

%package brocade
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for Brocade switches
Requires: openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
Recommends: telnet
%endif
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description brocade
Fence agent for Brocade devices that are accessed via telnet or SSH.
%files brocade
%{_sbindir}/fence_brocade
%{_mandir}/man8/fence_brocade.8*

%package cisco-mds
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for Cisco MDS 9000 series
Requires: net-snmp-utils
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description cisco-mds
Fence agent for Cisco MDS 9000 series devices that are accessed
via the SNMP protocol.
%files cisco-mds
%{_sbindir}/fence_cisco_mds
%{_mandir}/man8/fence_cisco_mds.8*

%package cisco-ucs
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for Cisco UCS series
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description cisco-ucs
Fence agent for Cisco UCS series devices that are accessed
via the SNMP protocol.
%files cisco-ucs
%{_sbindir}/fence_cisco_ucs
%{_mandir}/man8/fence_cisco_ucs.8*

%package drac5
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for Dell DRAC 5
Requires: openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
Recommends: telnet
%endif
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description drac5
Fence agent for Dell DRAC 5 series devices that are accessed
via telnet or SSH.
%files drac5
%{_sbindir}/fence_drac5
%{_mandir}/man8/fence_drac5.8*

%package eaton-snmp
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for Eaton network power switches
Requires: net-snmp-utils
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description eaton-snmp
Fence agent for Eaton network power switches that are accessed
via the SNMP protocol.
%files eaton-snmp
%{_sbindir}/fence_eaton_snmp
%{_mandir}/man8/fence_eaton_snmp.8*

%package emerson
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for Emerson devices (SNMP)
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description emerson
Fence agent for Emerson devices that are accessed via
the SNMP protocol.
%files emerson
%{_sbindir}/fence_emerson
%{_mandir}/man8/fence_emerson.8*

%package eps
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for ePowerSwitch 8M+ power switches
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description eps
Fence agent for ePowerSwitch 8M+ power switches that are accessed
via the HTTP(s) protocol.
%files eps
%{_sbindir}/fence_eps*
%{_mandir}/man8/fence_eps*.8*

%ifarch x86_64
%package gce
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for GCE (Google Cloud Engine)
Requires: fence-agents-common = %{version}-%{release}
Requires: ha-cloud-support = %{version}-%{release}
Obsoletes: fence-agents < 3.1.13
%description gce
Fence agent for GCE (Google Cloud Engine) instances.
%files gce
%{_sbindir}/fence_gce
%{_mandir}/man8/fence_gce.8*
%endif

%package heuristics-ping
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Pseudo fence agent to affect other agents based on ping-heuristics
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
Obsoletes: fence-agents < 3.1.13
%description heuristics-ping
Fence pseudo agent used to affect other agents based on
ping-heuristics.
%files heuristics-ping
%{_sbindir}/fence_heuristics_ping
%{_mandir}/man8/fence_heuristics_ping.8*

%package hpblade
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for HP BladeSystem devices
Requires: openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
Recommends: telnet
%endif
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description hpblade
Fence agent for HP BladeSystem devices that are accessed via telnet
or SSH.
%files hpblade
%{_sbindir}/fence_hpblade
%{_mandir}/man8/fence_hpblade.8*

%package ibmblade
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for IBM BladeCenter
Requires: net-snmp-utils
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description ibmblade
Fence agent for IBM BladeCenter devices that are accessed
via the SNMP protocol.
%files ibmblade
%{_sbindir}/fence_ibmblade
%{_mandir}/man8/fence_ibmblade.8*

%package ibm-powervs
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for IBM PowerVS
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description ibm-powervs
Fence agent for IBM PowerVS that are accessed via REST API.
%files ibm-powervs
%{_sbindir}/fence_ibm_powervs
%{_mandir}/man8/fence_ibm_powervs.8*

%package ibm-vpc
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for IBM Cloud VPC
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description ibm-vpc
Fence agent for IBM Cloud VPC that are accessed via REST API.
%files ibm-vpc
%{_sbindir}/fence_ibm_vpc
%{_mandir}/man8/fence_ibm_vpc.8*

%package ifmib
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for devices with IF-MIB interfaces
Requires: net-snmp-utils
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description ifmib
Fence agent for IF-MIB interfaces that are accessed via
the SNMP protocol.
%files ifmib
%{_sbindir}/fence_ifmib
%{_mandir}/man8/fence_ifmib.8*

%package ilo2
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agents for HP iLO2 devices
Requires: gnutls-utils
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description ilo2
Fence agents for HP iLO2 devices that are accessed via
the HTTP(s) protocol.
%files ilo2
%{_sbindir}/fence_ilo
%{_sbindir}/fence_ilo2
%{_mandir}/man8/fence_ilo.8*
%{_mandir}/man8/fence_ilo2.8*

%package ilo-moonshot
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for HP iLO Moonshot devices
Requires: openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
Recommends: telnet
%endif
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description ilo-moonshot
Fence agent for HP iLO Moonshot devices that are accessed
via telnet or SSH.
%files ilo-moonshot
%{_sbindir}/fence_ilo_moonshot
%{_mandir}/man8/fence_ilo_moonshot.8*

%package ilo-mp
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for HP iLO MP devices
Requires: openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
Recommends: telnet
%endif
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description ilo-mp
Fence agent for HP iLO MP devices that are accessed via telnet or SSH.
%files ilo-mp
%{_sbindir}/fence_ilo_mp
%{_mandir}/man8/fence_ilo_mp.8*

%package ilo-ssh
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agents for HP iLO devices over SSH
Requires: openssh-clients
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description ilo-ssh
Fence agents for HP iLO devices that are accessed via telnet or SSH.
%files ilo-ssh
%{_sbindir}/fence_ilo_ssh
%{_mandir}/man8/fence_ilo_ssh.8*
%{_sbindir}/fence_ilo3_ssh
%{_mandir}/man8/fence_ilo3_ssh.8*
%{_sbindir}/fence_ilo4_ssh
%{_mandir}/man8/fence_ilo4_ssh.8*
%{_sbindir}/fence_ilo5_ssh
%{_mandir}/man8/fence_ilo5_ssh.8*

%package intelmodular
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for devices with Intel Modular interfaces
Requires: net-snmp-utils
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description intelmodular
Fence agent for Intel Modular interfaces that are accessed
via the SNMP protocol.
%files intelmodular
%{_sbindir}/fence_intelmodular
%{_mandir}/man8/fence_intelmodular.8*

%package ipdu
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for IBM iPDU network power switches
Requires: net-snmp-utils
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description ipdu
Fence agent for IBM iPDU network power switches that are accessed
via the SNMP protocol.
%files ipdu
%{_sbindir}/fence_ipdu
%{_mandir}/man8/fence_ipdu.8*

%package ipmilan
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agents for devices with IPMI interface
Requires: /usr/bin/ipmitool
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description ipmilan
Fence agents for devices with IPMI interface.
%files ipmilan
%{_sbindir}/fence_ipmilan
%{_mandir}/man8/fence_ipmilan.8*
%{_sbindir}/fence_idrac
%{_mandir}/man8/fence_idrac.8*
%{_sbindir}/fence_ilo3
%{_mandir}/man8/fence_ilo3.8*
%{_sbindir}/fence_ilo4
%{_mandir}/man8/fence_ilo4.8*
%{_sbindir}/fence_ilo5
%{_mandir}/man8/fence_ilo5.8*
%{_sbindir}/fence_ipmilanplus
%{_mandir}/man8/fence_ipmilanplus.8*
%{_sbindir}/fence_imm
%{_mandir}/man8/fence_imm.8*

%package kdump
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for use with kdump crash recovery service
Requires: fence-agents-common = %{version}-%{release}
# this cannot be noarch since it's compiled
%description kdump
Fence agent for use with kdump crash recovery service.
%files kdump
%{_sbindir}/fence_kdump
%{_libexecdir}/fence_kdump_send
%{_mandir}/man8/fence_kdump.8*
%{_mandir}/man8/fence_kdump_send.8*

%package kubevirt
License: GPL-2.0-or-later AND LGPL-2.0-or-later AND Apache-2.0 AND MIT
Summary: Fence agent for KubeVirt platform
Requires: fence-agents-common = %{version}-%{release}
Requires: python3-pyyaml python3-pyasn1 python3-dateutil python3-urllib3 python3-six python3-requests python3-requests-oauthlib python3-charset-normalizer python3-oauthlib
Provides: bundled(python3-openshift) = 0.13.2
Provides: bundled(python3-kubernetes) = 29.0.0
Provides: bundled(python3-python-string-utils) = 1.0.0
Provides: bundled(python3-websocket-client) = 1.7.0
%description kubevirt
Fence agent for KubeVirt platform.
%files kubevirt
%{_sbindir}/fence_kubevirt
%{_mandir}/man8/fence_kubevirt.8*
# bundled libraries
%{_usr}/lib/%{name}/support/kubevirt/lib
%exclude %{_usr}/lib/%{name}/support/kubevirt/README

%package lpar
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for IBM LPAR
Requires: openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
Recommends: telnet
%endif
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description lpar
Fence agent for IBM LPAR devices that are accessed via telnet or SSH.
%files lpar
%{_sbindir}/fence_lpar
%{_mandir}/man8/fence_lpar.8*

%package mpath
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for reservations over Device Mapper Multipath
Requires: device-mapper-multipath
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description mpath
Fence agent for SCSI persistent reservation over
Device Mapper Multipath.
%files mpath
%{_sbindir}/fence_mpath
%{_datadir}/cluster/fence_mpath_check*
%{_mandir}/man8/fence_mpath.8*

%ifarch x86_64 ppc64le
%package openstack
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for OpenStack's Nova service
Requires: python3-requests
Requires: fence-agents-common = %{version}-%{release}
Obsoletes: ha-openstack-support <= %{version}-%{release}
%description openstack
Fence agent for OpenStack's Nova service.
%files openstack
%{_sbindir}/fence_openstack
%{_mandir}/man8/fence_openstack.8*
%endif

%package redfish
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Group: System Environment/Base
Summary: Fence agent for Redfish
Requires: fence-agents-common >= %{version}-%{release}
Requires: python3-requests
Obsoletes: fence-agents < 3.1.13
%description redfish
The fence-agents-redfish package contains a fence agent for Redfish
%files redfish
%defattr(-,root,root,-)
%{_sbindir}/fence_redfish
%{_mandir}/man8/fence_redfish.8*

%package rhevm
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for RHEV-M
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description rhevm
Fence agent for RHEV-M via REST API.
%files rhevm
%{_sbindir}/fence_rhevm
%{_mandir}/man8/fence_rhevm.8*

%package rsa
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for IBM RSA II
Requires: openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
Recommends: telnet
%endif
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description rsa
Fence agent for IBM RSA II devices that are accessed
via telnet or SSH.
%files rsa
%{_sbindir}/fence_rsa
%{_mandir}/man8/fence_rsa.8*

%package rsb
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for Fujitsu RSB
Requires: openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
Recommends: telnet
%endif
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description rsb
Fence agent for Fujitsu RSB devices that are accessed
via telnet or SSH.
%files rsb
%{_sbindir}/fence_rsb
%{_mandir}/man8/fence_rsb.8*

%package sbd
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for SBD (storage-based death)
Requires: sbd
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description sbd
Fence agent for SBD (storage-based death).
%files sbd
%{_sbindir}/fence_sbd
%{_mandir}/man8/fence_sbd.8*

%package scsi
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for SCSI persistent reservations
Requires: sg3_utils
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description scsi
Fence agent for SCSI persistent reservations.
%files scsi
%{_sbindir}/fence_scsi
%{_datadir}/cluster/fence_scsi_check
%{_datadir}/cluster/fence_scsi_check_hardreboot
%{_mandir}/man8/fence_scsi.8*

# skipped from allfenceagents
%package virsh
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for virtual machines based on libvirt
Requires: openssh-clients /usr/bin/virsh
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description virsh
Fence agent for virtual machines that are accessed via SSH.
%files virsh
%{_sbindir}/fence_virsh
%{_mandir}/man8/fence_virsh.8*

%package vmware-rest
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for VMWare with REST API
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
Obsoletes: fence-agents < 3.1.13
%description vmware-rest
Fence agent for VMWare with REST API.
%files vmware-rest
%{_sbindir}/fence_vmware_rest
%{_mandir}/man8/fence_vmware_rest.8*

%package vmware-soap
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for VMWare with SOAP API v4.1+
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description vmware-soap
Fence agent for VMWare with SOAP API v4.1+.
%files vmware-soap
%{_sbindir}/fence_vmware_soap
%{_mandir}/man8/fence_vmware_soap.8*

%package wti
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for WTI Network power switches
Requires: openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
Recommends: telnet
%endif
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description wti
Fence agent for WTI network power switches that are accessed
via telnet or SSH.
%files wti
%{_sbindir}/fence_wti
%{_mandir}/man8/fence_wti.8*

%ifarch s390x
%package zvm
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for IBM z/VM over IP
Requires: fence-agents-common = %{version}-%{release}
%description zvm
Fence agent for IBM z/VM over IP.
%files zvm
%{_sbindir}/fence_zvmip
%{_mandir}/man8/fence_zvmip.8*
%endif

# fence-virt

%ifarch x86_64
%package -n fence-virt
Summary: A pluggable fencing framework for virtual machines
Requires(post):	systemd-sysv %{systemd_units}
Requires(preun):	%{systemd_units}
Requires(postun):	%{systemd_units}
%description -n fence-virt
Fencing agent for virtual machines.
%files -n fence-virt
%doc agents/virt/docs/*
%{_sbindir}/fence_virt
%{_sbindir}/fence_xvm
%{_mandir}/man8/fence_virt.*
%{_mandir}/man8/fence_xvm.*

%package -n fence-virtd
Summary: Daemon which handles requests from fence-virt
%description -n fence-virtd
This package provides the host server framework, fence_virtd,
for fence_virt.  The fence_virtd host daemon is resposible for
processing fencing requests from virtual machines and routing
the requests to the appropriate physical machine for action.
%files -n fence-virtd
%{_sbindir}/fence_virtd
%{_unitdir}/fence_virtd.service
%config(noreplace) %{_sysconfdir}/fence_virt.conf
%dir %{_libdir}/fence-virt
%{_libdir}/fence-virt/vsock.so
%{_mandir}/man5/fence_virt.conf.*
%{_mandir}/man8/fence_virtd.*

%package -n fence-virtd-multicast
Summary:  Multicast listener for fence-virtd
Requires: fence-virtd
%description -n fence-virtd-multicast
Provides multicast listener capability for fence-virtd.
%files -n fence-virtd-multicast
%{_libdir}/fence-virt/multicast.so

%package -n fence-virtd-serial
Summary:  Serial VMChannel listener for fence-virtd
Requires: libvirt >= 0.6.2
Requires: fence-virtd
%description -n fence-virtd-serial
Provides serial VMChannel listener capability for fence-virtd.
%files -n fence-virtd-serial
%{_libdir}/fence-virt/serial.so

%package -n fence-virtd-tcp
Summary:  TCP listener for fence-virtd
Requires: fence-virtd
%description -n fence-virtd-tcp
Provides TCP listener capability for fence-virtd.
%files -n fence-virtd-tcp
%{_libdir}/fence-virt/tcp.so

%package -n fence-virtd-libvirt
Summary:  Libvirt backend for fence-virtd
Requires: libvirt >= 0.6.0
Requires: fence-virtd
%description -n fence-virtd-libvirt
Provides fence_virtd with a connection to libvirt to fence
virtual machines.  Useful for running a cluster of virtual
machines on a desktop.
%files -n fence-virtd-libvirt
%{_libdir}/fence-virt/virt.so

%package -n fence-virtd-cpg
Summary:  CPG/libvirt backend for fence-virtd
Requires: corosynclib
Requires: fence-virtd
%description -n fence-virtd-cpg
Provides fence_virtd with a connection to libvirt to fence
virtual machines. Uses corosync CPG to keep track of VM
locations to allow for non-local VMs to be fenced when VMs
are located on corosync cluster nodes.
%files -n fence-virtd-cpg
%{_libdir}/fence-virt/cpg.so
%endif

%changelog
* Wed Aug 20 2025 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.16.0-5.5
- fence_aws: add "skip_os_shutdown" parameter to allow hard poweroff
  Resolves: RHEL-109922

* Tue Aug 12 2025 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.16.0-5.4
- fence_ibm_vpc: add apikey file support
  Resolves: RHEL-107530

* Thu Jul 17 2025 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.16.0-5.3
- fence_ibm_vpc: refresh bearer-token if token data is corrupt, and
  avoid edge-case of writing empty token file
  Resolves: RHEL-83774

* Mon Feb  3 2025 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.16.0-5
- fence_azure_arm: use azure-identity instead of msrestazure, which has
  been deprecated
  Resolves: RHEL-76495

* Tue Nov 26 2024 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.16.0-2
- Move fence-agents to AppStream
  Resolves: RHEL-68842

* Mon Nov 25 2024 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.16.0-1
- new upstream release
  Resolves: RHEL-65332
- ha-cloud-support: add awscli2 dependency
  Resolves: RHEL-60021
- fence_bladecenter fix SyntaxWarning: invalid escape sequence '\s'
  Resolves: RHEL-57063
- build: remove python-poetry-core BuildRequires
  Resolves: RHEL-60893

* Tue Oct 29 2024 Troy Dawson <tdawson@redhat.com> - 4.15.0-2
- Bump release for October 2024 mass rebuild:
  Resolves: RHEL-64018

* Tue Jul  2 2024 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.15.0-1
- new upstream release
  Resolves: RHEL-45835

* Mon Jun 24 2024 Troy Dawson <tdawson@redhat.com> - 4.13.1-8
- Bump release for June 2024 mass rebuild

* Wed May 15 2024 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.13.1-7
- lib/all agents: use r"" to avoid SyntaxWarnings 
  Resolves: RHEL-35663
- fix pycurl bundled path
  Resolves: RHEL-35986

* Mon Apr 15 2024 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.13.1-6
- Bundled missing libraries
  Resolves: RHEL-25954

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 17 2023 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.13.1-1
- new upstream release
