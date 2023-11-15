# Copyright 2004-2011 Red Hat, Inc.
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions
# of the GNU General Public License v.2.

# keep around ready for later user
## global alphatag git0a6184070

# bundles
%global bundled_lib_dir    bundled
# alibaba
# python-pycryptodome bundle
%global pycryptodome		pycryptodome
%global pycryptodome_version	3.6.4
%global pycryptodome_dir	%{bundled_lib_dir}/aliyun/%{pycryptodome}
# python-aliyun-sdk-core bundle
%global aliyunsdkcore		aliyun-python-sdk-core
%global aliyunsdkcore_version	2.13.1
%global aliyunsdkcore_dir	%{bundled_lib_dir}/aliyun/%{aliyunsdkcore}
# python-aliyun-sdk-ecs bundle
%global aliyunsdkecs		aliyun-python-sdk-ecs
%global aliyunsdkecs_version	4.9.3
%global aliyunsdkecs_dir	%{bundled_lib_dir}/aliyun/%{aliyunsdkecs}
# python-aliyun-sdk-vpc bundle
%global aliyunsdkvpc		aliyun-python-sdk-vpc
%global aliyunsdkvpc_version	3.0.2
%global aliyunsdkvpc_dir	%{bundled_lib_dir}/aliyun/%{aliyunsdkvpc}
# aws
%global botocore		botocore
%global botocore_version	1.23.46
%global chardet 		chardet
%global chardet_version 	4.0.0
## for pip install only
%global jmespath		jmespath
%global jmespath_version	0.10.0
# google cloud
%global httplib2		httplib2
%global httplib2_version	0.19.1
# kubevirt
%global openshift		openshift
%global openshift_version	0.12.1
%global ruamelyamlclib		ruamel.yaml.clib
%global ruamelyamlclib_version	0.2.6
%global kubernetes		kubernetes
%global kubernetes_version	12.0.1
%global certifi			certifi
%global certifi_version		2021.10.8
%global googleauth		google-auth
%global googleauth_version	2.3.0
%global cachetools		cachetools
%global cachetools_version	4.2.4
%global pyasn1modules		pyasn1-modules
%global pyasn1modules_version	0.2.8
%global pyasn1			pyasn1
%global pyasn1_version		0.4.8
%global dateutil		dateutil
%global dateutil_version	2.8.2
%global pyyaml			PyYAML
%global pyyaml_version		6.0
%global six			six
%global six_version		1.16.0
%global urllib3			urllib3
%global urllib3_version		1.26.7
%global websocketclient		websocket-client
%global websocketclient_version	1.2.1
%global jinja2			Jinja2
%global jinja2_version		3.0.2
%global markupsafe		MarkupSafe
%global markupsafe_version	2.0.1
%global stringutils		string-utils
%global stringutils_version	1.0.0
%global requests		requests
%global requests_version	2.26.0
%global chrstnormalizer		charset-normalizer
%global chrstnormalizer_version	2.0.7
%global idna			idna
%global idna_version		3.3
%global reqstsoauthlib		requests-oauthlib
%global reqstsoauthlib_version	1.3.0
%global oauthlib		oauthlib
%global oauthlib_version	3.1.1
%global ruamelyaml		ruamel.yaml
%global ruamelyaml_version	0.17.16
%global setuptools		setuptools
%global setuptools_version	58.3.0

Name: fence-agents
Summary: Set of unified programs capable of host isolation ("fencing")
Version: 4.2.1
Release: 121%{?alphatag:.%{alphatag}}%{?dist}
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
URL: https://github.com/ClusterLabs/fence-agents
Source0: https://fedorahosted.org/releases/f/e/fence-agents/%{name}-%{version}.tar.gz
# aliyun
Source1: %{pycryptodome}-%{pycryptodome_version}.tar.gz
Source2: %{aliyunsdkcore}-%{aliyunsdkcore_version}.tar.gz
Source3: %{aliyunsdkecs}-%{aliyunsdkecs_version}.tar.gz
Source4: %{aliyunsdkvpc}-%{aliyunsdkvpc_version}.tar.gz
# google cloud
Source5: %{httplib2}-%{httplib2_version}-py3-none-any.whl
Source6: pyparsing-2.4.7-py2.py3-none-any.whl
# aws
Source7: %{botocore}-%{botocore_version}.tar.gz
Source8: %{jmespath}-%{jmespath_version}.tar.gz
Source9: %{chardet}-%{chardet_version}.tar.gz
# kubevirt
## pip download --no-binary :all: openshift "ruamel.yaml.clib>=0.1.2"
### BEGIN
Source10: %{openshift}-%{openshift_version}.tar.gz
Source11: %{ruamelyamlclib}-%{ruamelyamlclib_version}.tar.gz
Source12: %{kubernetes}-%{kubernetes_version}.tar.gz
Source13: %{certifi}-%{certifi_version}.tar.gz
Source14: %{googleauth}-%{googleauth_version}.tar.gz
Source15: %{cachetools}-%{cachetools_version}.tar.gz
Source16: %{pyasn1modules}-%{pyasn1modules_version}.tar.gz
Source17: %{pyasn1}-%{pyasn1_version}.tar.gz
Source18: python-%{dateutil}-%{dateutil_version}.tar.gz
Source19: %{pyyaml}-%{pyyaml_version}.tar.gz
## rsa is dependency for "pip install",
## but gets removed to use cryptography lib instead
Source20: rsa-4.7.2.tar.gz
Source21: %{six}-%{six_version}.tar.gz
Source22: %{urllib3}-%{urllib3_version}.tar.gz
Source23: %{websocketclient}-%{websocketclient_version}.tar.gz
Source24: %{jinja2}-%{jinja2_version}.tar.gz
Source25: %{markupsafe}-%{markupsafe_version}.tar.gz
Source26: python-%{stringutils}-%{stringutils_version}.tar.gz
Source27: %{requests}-%{requests_version}.tar.gz
Source28: %{chrstnormalizer}-%{chrstnormalizer_version}.tar.gz
Source29: %{idna}-%{idna_version}.tar.gz
Source30: %{reqstsoauthlib}-%{reqstsoauthlib_version}.tar.gz
Source31: %{oauthlib}-%{oauthlib_version}.tar.gz
Source32: %{ruamelyaml}-%{ruamelyaml_version}.tar.gz
Source33: %{setuptools}-%{setuptools_version}.tar.gz
## required for installation
Source34: setuptools_scm-6.3.2.tar.gz
Source35: packaging-21.2-py3-none-any.whl
Source36: tomli-1.0.1.tar.gz
### END

Patch0: fence_impilan-fence_ilo_ssh-add-ilo5-support.patch
Patch1: fence_mpath-watchdog-support.patch
Patch2: fence_ilo3-fence_ipmilan-show-correct-default-method.patch
Patch3: fence_evacuate-fix-evacuable-tag-mix-issue.patch
Patch4: fence_compute-fence_evacuate-fix-compute-domain.patch
Patch5: fence_gce-1-stackdriver-logging-default-method-cycle.patch
Patch6: fence_gce-2-filter-aggregatedlist.patch
Patch7: fence_aliyun-1.patch
Patch8: fence_aliyun-2.patch
Patch9: fence_aliyun-3-logging.patch
Patch10: fence_aliyun-4-bundled.patch
Patch11: python3-has_key-fixes.patch
Patch12: fence_kdump-fix-strncpy-issue.patch
Patch13: fix-version.patch
Patch14: fence_gce-3-stackdriver-logging-note.patch
Patch15: fence_aliyun-5-list-instance-names.patch
Patch16: fence_aliyun-6-correct-help-indentation.patch
Patch17: fence_cisco_ucs-encode-POSTFIELDS.patch
Patch18: bz1654968-fence_scsi-fix-incorrect-SCSI-key-node-ID-10-or-higher.patch
Patch19: bz1654976-1-fence_scsi-watchdog-retry-support.patch
Patch20: bz1654976-2-build-fix-check_used_options.patch
Patch21: bz1654616-fence_hpblade-fix-log_expect_syntax.patch
Patch22: bz1654973-fence_vmware_soap-cleanup-sigterm.patch
Patch23: bz1650214-fence_azure_arm-bundled.patch
Patch24: bz1666914-1-fence_redfish.patch
Patch25: bz1666914-2-fence_redfish-fail-invalid-cert.patch
Patch26: bz1677327-1-fence_redfish-use-ipport-parameter.patch
Patch27: bz1677327-2-fence_redfish-ip-parameter-backward-compatibility.patch
Patch28: bz1696584-fence_gce-fix-python3-encoding-issue.patch
Patch29: bz1709926-fence_mpath-fix-watchdog-hardreboot.patch
Patch30: bz1709780-fence_rhevm-RHEV-v4-API-support.patch
Patch31: bz1712263-fence_rhevm-1-use-UTF8-encoding.patch
Patch32: bz1712263-fence_rhevm-2-fix-debug-encoding-issues.patch
Patch33: bz1700546-fence_azure_arm-skip_shutdown.patch
Patch34: bz1704228-fence_redfish-full-redfish-spec-compliance.patch
Patch35: bz1714458-fence_scsi-node-id-new-format.patch
Patch36: bz1720198-fence_scsi-watchdog-fix-retry-failing-on-first-try.patch
Patch37: bz1732773-fence_vmware_rest-fix-keyerror-suspended-vms.patch
Patch38: bz1748443-fence_zvmip-python3-fixes.patch
Patch39: bz1732766-fence_aliyun-1-add-RAM-role.patch
Patch40: bz1732766-fence_aliyun-2-import-EcsRamRoleCredential.patch
Patch41: bz1734811-fence_iloX_ssh-monitor-timeout-warning.patch
Patch42: bz1751704-fence_mpath-fix-watchdog-trigger-multipath-disconnect.patch
Patch43: bz1760213-fence_compute-disable-service-after-force-down.patch
Patch44: bz1760201-fence_compute-fence_evacuate-1-fix-region_name-type.patch
Patch45: bz1760224-fence_vmware_rest-improve-logging.patch
Patch46: bz1760201-fence_compute-fence_evacuate-2-fix-project-shortopt.patch
Patch47: bz1769783-fencing-improve-stdin-quote-parsing.patch
Patch48: bz1763674-fence_rhevm-add-cookie-support.patch
Patch49: bz1773890-fence_scsi-add-hash-key-value-support.patch
Patch50: bz1774458-fence_sbd-stderr-support.patch
Patch51: bz1771594-1-fencing-inetX_only-SSH-fence_zvmip.patch
Patch52: bz1771594-2-fence_redfish-fence_vmware_soap-suppress-warning.patch
Patch53: bz1781357-fence_aws-improve-logging-and-metadata-usage-text.patch
Patch54: bz1753228-fence_mpath-1-add-plug-parameter-support.patch
Patch55: bz1753228-fence_mpath-2-fix-plug-parameter-issues.patch
Patch56: bz1798641-fence_mpath-fix-reserve-parameter-typo.patch
Patch57: bz1810457-fence_aws-improve-parameter-logic.patch
Patch58: bz1816203-fence_aws-1-fix-race-condition.patch
Patch59: bz1816203-fence_aws-2-fix-python3-encoding.patch
Patch60: bz1827559-fence_vmware_rest-improve-exception-handling.patch
Patch61: bz1827652-fence_vmware_rest-1-add-filter-parameter.patch
Patch62: bz1827652-fence_vmware_rest-2-fix-1000-VM-monitor-error.patch
Patch63: bz1830776-fence_compute-fence_evacuate-fix-insecure-parameter.patch
Patch64: bz1750596-fence_scsi-add-readonly-parameter.patch
Patch65: bz1793739-fence_vmware_rest-1-fix-encoding.patch
Patch66: bz1793739-fence_vmware_rest-2-support-utf-8-vm-names.patch
Patch67: bz1839776-fence_aws-catch-connectionerror.patch
Patch68: bz1796654-fence_vmware_soap-log-exception-message-for-SSLError.patch
Patch69: bz1793739-fence_vmware_rest-3-fix-encode-issue.patch
Patch70: bz1860544-fence_lpar-fix-long-user-host-issue.patch
Patch71: bz1859932-fence_evacuate-support-private-flavors.patch
Patch72: bz1818157-fence_azure_arm-fix-MSI-support.patch
Patch73: bz1851115-fence_mpath-support-comma-and-space-separated-devices.patch
Patch74: bz1853973-fence_ipmilan-allow-increasing-ipmitool-verbosity.patch
Patch75: bz1861926-fence_lpar-fix-list-status-action.patch
Patch76: bz1470813-fencing-1-disable-timeout.patch
Patch77: bz1470813-fencing-2-fix-power-timeout.patch
Patch78: bz1470813-fencing-3-make-timeout-0-mean-forever.patch
Patch79: bz1470813-fencing-4-make-timeout-0-mean-forever.patch
Patch80: bz1841087-fence_scsi-dont-write-key-device-to-file.patch
Patch81: bz1896827-fence_aws-add-imdsv2-support.patch
Patch82: bz1914313-fence_zvmip-fix-disable-timeout.patch
Patch83: bz1906978-fence_gce-default-to-onoff.patch
Patch84: bz1925015-fence_ipmilan-add-fence_ipmilanplus.patch
Patch85: bz1920947-fence_redfish-1-add-diag-action.patch
Patch86: bz1941989-fence_aws-add-filter-parameter.patch
Patch87: bz1780825-fencing-1-add-stonith_status_sleep.patch
Patch88: bz1780825-fencing-2-metadata-fix-long-parameters.patch
Patch89: bz1942363-fence_gce-default-to-cycle.patch
Patch90: bz1920947-fence_redfish-2-add-diag-action-logic.patch
Patch91: bz1920947-fence_redfish-3-fix-typo.patch
Patch92: bz1922437-fence_mpath-watchdog-retry-support.patch
Patch93: bz1685814-fence_gce-add-serviceaccount-file-support.patch
Patch94: bz1728203-bz1874862-fence_ibm_vpc-fence_ibm_powervs.patch
Patch95: bz1969953-fence_gce-1-add-proxy-support.patch
Patch96: bz1969953-fence_gce-2-bundled.patch
Patch97: bz1470827-all-agents-log-exceptions-fail.patch
Patch98: bz2010710-1-fence_amt_ws-fix-or-dead-code.patch
Patch99: bz2010710-2-fence_amt_ws-boot-option.patch
Patch100: bz1969953-fence_gce-3-fix-httplib2-import.patch
Patch101: bz1971683-fence_sbd-dont-spam-logs-disable-timeout.patch
Patch102: bz1977588-1-fencing-add-EC_FETCH_VM_UUID.patch
Patch103: bz1977588-2-fence_kubevirt.patch
Patch104: bz1977588-3-fence_kubevirt-fix-status.patch
Patch105: bz1977588-4-fence_kubevirt-power-timeout-40s.patch
Patch106: bz1963163-fence_zvmip-add-ssl-tls-support.patch
Patch107: bz1977588-5-fence_kubevirt-get-namespace-from-context.patch
Patch108: bz2048857-fence_aws-botocore-bundled.patch
Patch109: bz1886074-1-fencing-source_env.patch
Patch110: bz1886074-2-fence_openstack.patch
Patch111: bz2072421-1-all-agents-unify-ssl-parameters.patch
Patch112: bz2078244-fence_gce-update.patch
Patch113: bz2080994-fence_ibm_vpc-fix-parameters.patch
Patch114: bz2080729-1-fence_apc-fence_ilo_moonshot-import-logging.patch
Patch115: bz2080729-2-fence_lpar-fix-import-fail_usage.patch
Patch116: bz2072421-2-fence_zvmip-connect-error.patch
Patch117: bz2091826-fence_ibm_vpc-add-proxy-support.patch
Patch118: bz2092921-fence_ibm_powervs-proxy-private-api-servers.patch
Patch119: bz1886074-4-fencing-source_env-dont-process-empty-lines.patch
Patch120: bz1787178-1-fence_vmware_soap-set-timeout-cleanup-tmp-dirs.patch
Patch121: bz1787178-2-fence_vmware_soap-login-timeout-15s.patch
Patch122: bz2102024-fence_ibm_vpc-add-token-cache-support.patch
Patch123: bz2134017-fence_lpar-only-output-additional-info-on-debug.patch
Patch124: bz2136076-fence_ibm_powervs-improve-defaults.patch
Patch125: bz2160478-fence_scsi-fix-validate-all.patch
Patch126: bz2152105-fencing-1-add-plug_separator.patch
Patch127: bz2152105-fencing-2-update-DEPENDENCY_OPT.patch
Patch128: bz2183158-fence_aws-1-add-skip-race-check-parameter.patch
Patch129: bz2183158-fence_aws-2-fail-when-power-action-request-fails.patch
Patch130: bz2187329-fence_scsi-1-detect-devices-in-shared-vgs.patch
Patch131: bz2187329-fence_scsi-2-support-space-separated-devices.patch
Patch132: bz2211460-fence_azure-arm-1-stack-hub-support.patch
Patch133: bz2211460-fence_azure-arm-2-metadata-endpoint-error-message.patch
Patch134: bz2155453-fence_ibm_powervs-performance-improvements.patch

### HA support libs/utils ###
Patch1000: bz2218234-1-aws-fix-bundled-dateutil-CVE-2007-4559.patch
Patch1001: bz2218234-2-kubevirt-fix-bundled-dateutil-CVE-2007-4559.patch

%if 0%{?fedora} || 0%{?rhel} > 7
%global supportedagents amt_ws apc apc_snmp bladecenter brocade cisco_mds cisco_ucs compute drac5 eaton_snmp emerson eps evacuate hds_cb hpblade ibmblade ibm_powervs ibm_vpc ifmib ilo ilo_moonshot ilo_mp ilo_ssh intelmodular ipdu ipmilan kdump kubevirt lpar mpath redfish rhevm rsa rsb sbd scsi vmware_rest vmware_soap wti
%ifarch x86_64
%global testagents virsh heuristics_ping aliyun aws azure_arm gce openstack
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

%global allfenceagents %(cat <<EOF
fence-agents-amt-ws \\
fence-agents-apc \\
fence-agents-apc-snmp \\
fence-agents-bladecenter \\
fence-agents-brocade \\
fence-agents-cisco-mds \\
fence-agents-cisco-ucs \\
fence-agents-compute \\
fence-agents-drac5 \\
fence-agents-eaton-snmp \\
fence-agents-emerson \\
fence-agents-eps \\
fence-agents-heuristics-ping \\
fence-agents-hpblade \\
fence-agents-ibmblade \\
fence-agents-ifmib \\
fence-agents-ilo2 \\
fence-agents-ilo-moonshot \\
fence-agents-ilo-mp \\
fence-agents-ilo-ssh \\
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
%endif

# Build dependencies
## general
BuildRequires: autoconf automake libtool
## compiled code (-kdump)
BuildRequires: gcc
## man pages generating
BuildRequires: libxslt
## establishing proper paths to particular programs
BuildRequires: gnutls-utils
## Python dependencies
BuildRequires: python3-devel
BuildRequires: python3-pexpect python3-pycurl python3-requests
BuildRequires: python3-suds openwsman-python3 python3-boto3
BuildRequires: python3-google-api-client python3-pip python3-wheel python3-jinja2

# turn off the brp-python-bytecompile script
# (for F28+ or equivalent, the latter is the preferred form)
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompilespace:.*$!!g')
#undefine __brp_python_bytecompile

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1 -F2
%patch31 -p1 -F2
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1 -F1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1 -F2
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1 -F1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1 -F1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1 -F1
%patch66 -p1
%patch67 -p1
%patch68 -p1
%patch69 -p1
%patch70 -p1
%patch71 -p1
%patch72 -p1
%patch73 -p1
%patch74 -p1
%patch75 -p1
%patch76 -p1
%patch77 -p1
%patch78 -p1
%patch79 -p1
%patch80 -p1
%patch81 -p1
%patch82 -p1
%patch83 -p1
%patch84 -p1
%patch85 -p1
%patch86 -p1 -F1
%patch87 -p1
%patch88 -p1
%patch89 -p1
%patch90 -p1
%patch91 -p1
%patch92 -p1
%patch93 -p1
%patch94 -p1
%patch95 -p1
%patch96 -p1 -F2
%patch97 -p1
%patch98 -p1
%patch99 -p1
%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1 -F1
%patch105 -p1
%patch106 -p1
%patch107 -p1
%patch108 -p1
%patch109 -p1
%patch110 -p1
%patch111 -p1
%patch112 -p1
%patch113 -p1
%patch114 -p1
%patch115 -p1
%patch116 -p1
%patch117 -p1
%patch118 -p1
%patch119 -p1
%patch120 -p1
%patch121 -p1
%patch122 -p1 -F2
%patch123 -p1
%patch124 -p1
%patch125 -p1
%patch126 -p1
%patch127 -p1
%patch128 -p1 -F2
%patch129 -p1
%patch130 -p1
%patch131 -p1
%patch132 -p1
%patch133 -p1
%patch134 -p1

# prevent compilation of something that won't get used anyway
sed -i.orig 's|FENCE_ZVM=1|FENCE_ZVM=0|' configure.ac

%ifarch x86_64
# bundles
mkdir -p %{bundled_lib_dir}/aliyun

# python-pycryptodome bundle
tar -xzf %SOURCE1 -C %{bundled_lib_dir}
mv %{bundled_lib_dir}/%{pycryptodome}-%{pycryptodome_version} %{pycryptodome_dir}
cp %{pycryptodome_dir}/README.rst %{pycryptodome}_README.rst
cp %{pycryptodome_dir}/LICENSE.rst %{pycryptodome}_LICENSE.rst

# python-aliyun-sdk-core bundle
tar -xzf %SOURCE2 -C %{bundled_lib_dir}
mv %{bundled_lib_dir}/%{aliyunsdkcore}-%{aliyunsdkcore_version} %{aliyunsdkcore_dir}
cp %{aliyunsdkcore_dir}/README.rst %{aliyunsdkcore}_README.rst

# python-aliyun-sdk-ecs bundle
tar -xzf %SOURCE3 -C %{bundled_lib_dir}
mv %{bundled_lib_dir}/%{aliyunsdkecs}-%{aliyunsdkecs_version} %{aliyunsdkecs_dir}
cp %{aliyunsdkecs_dir}/README.rst %{aliyunsdkecs}_README.rst

# python-aliyun-sdk-vpc bundle
tar -xzf %SOURCE4 -C %{bundled_lib_dir}
mv %{bundled_lib_dir}/%{aliyunsdkvpc}-%{aliyunsdkvpc_version} %{aliyunsdkvpc_dir}
cp %{aliyunsdkvpc_dir}/README.rst %{aliyunsdkvpc}_README.rst
%endif

%build
./autogen.sh
%{configure} PYTHON="%{__python3}" \
%if %{defined _tmpfilesdir}
	SYSTEMD_TMPFILES_DIR=%{_tmpfilesdir} \
	--with-fencetmpdir=/run/fence-agents \
%endif
	--with-agents='%{supportedagents} %{testagents}'

CFLAGS="$(echo '%{optflags}')" make %{_smp_mflags}

%ifarch x86_64
# python-pycryptodome bundle
pushd %{pycryptodome_dir}
%{__python3} setup.py build
popd

# python-aliyun-sdk-core bundle
pushd %{aliyunsdkcore_dir}
%{__python3} setup.py build
popd

# python-aliyun-sdk-ecs bundle
pushd %{aliyunsdkecs_dir}
%{__python3} setup.py build
popd

# python-aliyun-sdk-vpc bundle
pushd %{aliyunsdkvpc_dir}
%{__python3} setup.py build
popd
%endif

%install
make install DESTDIR=%{buildroot}
# bytecompile Python source code in a non-standard location
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/fence
# XXX unsure if /usr/sbin/fence_* should be compiled as well

%ifarch x86_64
# python-pycryptodome bundle
pushd %{pycryptodome_dir}
%{__python3} setup.py install -O1 --skip-build --root %{buildroot} --install-lib /usr/lib/fence-agents/%{bundled_lib_dir}/aliyun
popd

# python-aliyun-sdk-core bundle
pushd %{aliyunsdkcore_dir}
%{__python3} setup.py install -O1 --skip-build --root %{buildroot} --install-lib /usr/lib/fence-agents/%{bundled_lib_dir}/aliyun
popd

# python-aliyun-sdk-ecs bundle
pushd %{aliyunsdkecs_dir}
%{__python3} setup.py install -O1 --skip-build --root %{buildroot} --install-lib /usr/lib/fence-agents/%{bundled_lib_dir}/aliyun
popd

# python-aliyun-sdk-vpc bundle
pushd %{aliyunsdkvpc_dir}
%{__python3} setup.py install -O1 --skip-build --root %{buildroot} --install-lib /usr/lib/fence-agents/%{bundled_lib_dir}/aliyun
popd

# google cloud
## for httplib2 install only
%{__python3} -m pip install --user --no-index --find-links %{_sourcedir} pyparsing
%{__python3} -m pip install --target %{buildroot}/usr/lib/fence-agents/%{bundled_lib_dir}/google --no-index --find-links %{_sourcedir} httplib2
%endif

# aws/kubevirt
%{__python3} -m pip install --user --no-index --find-links %{_sourcedir} setuptools-scm

# aws
%ifarch x86_64
%{__python3} -m pip install --user --no-index --find-links %{_sourcedir} jmespath
%{__python3} -m pip install --target %{buildroot}/usr/lib/fence-agents/%{bundled_lib_dir}/aws --no-index --find-links %{_sourcedir} botocore
%{__python3} -m pip install --target %{buildroot}/usr/lib/fence-agents/%{bundled_lib_dir}/aws --no-index --find-links %{_sourcedir} requests

# regular patch doesnt work in install-section
# Patch1000
pushd %{buildroot}/usr/lib/fence-agents/%{bundled_lib_dir}
/usr/bin/patch --no-backup-if-mismatch -p1 --fuzz=0 < %{_sourcedir}/bz2218234-1-aws-fix-bundled-dateutil-CVE-2007-4559.patch
popd
%endif

# kubevirt
%{__python3} -m pip install --target %{buildroot}/usr/lib/fence-agents/%{bundled_lib_dir}/kubevirt --no-index --find-links %{_sourcedir} openshift
rm -rf %{buildroot}/usr/lib/fence-agents/%{bundled_lib_dir}/kubevirt/rsa*
# Patch1001
pushd %{buildroot}/usr/lib/fence-agents/%{bundled_lib_dir}
/usr/bin/patch --no-backup-if-mismatch -p1 --fuzz=0 < %{_sourcedir}/bz2218234-2-kubevirt-fix-bundled-dateutil-CVE-2007-4559.patch
popd

## tree fix up
# fix libfence permissions
chmod 0755 %{buildroot}%{_datadir}/fence/*.py
# remove docs
rm -rf %{buildroot}/usr/share/doc/fence-agents

%post
ccs_update_schema > /dev/null 2>&1 ||:

%description
A collection of executables to handle isolation ("fencing") of possibly
misbehaving hosts by the means of remote power management, blocking
network, storage, or similar. They operate through a unified interface
(calling conventions) devised for the original Red Hat clustering solution.

%package common
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Common base for Fence Agents
Requires: python3-pexpect python3-pycurl
BuildArch: noarch
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
%exclude %{_datadir}/fence/XenAPI.*
%exclude %{_datadir}/fence/__pycache__/XenAPI.*
%{_datadir}/cluster
%exclude %{_datadir}/cluster/fence_mpath_check*
%exclude %{_datadir}/cluster/fence_scsi_check*
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

%package all
License: GPLv2+ and LGPLv2+ and ASL 2.0
Group: System Environment/Base
Summary: Set of unified programs capable of host isolation ("fencing")
Requires: %(echo "%{allfenceagents}" | sed "s/\( \|$\)/ >= %{version}-%{release}\1/g")
%ifarch i686 x86_64
Requires: fence-virt
%endif
%ifarch ppc64le
Requires: fence-agents-lpar >= %{version}-%{release}
%endif
%ifarch s390x
Requires: fence-agents-zvm >= %{version}-%{release}
%endif
Provides: %{name} >= %{version}-%{release}
Obsoletes: %{name} < %{version}-%{release}
%description all
A collection of executables to handle isolation ("fencing") of possibly
misbehaving hosts by the means of remote power management, blocking
network, storage, or similar.

This package serves as a catch-all for all supported fence agents.
%files all

%ifarch x86_64
%package aliyun
License: GPLv2+ and LGPLv2+ and ASL 2.0 and BSD and MIT
Group: System Environment/Base
Summary: Fence agent for Alibaba Cloud (Aliyun)
Requires: fence-agents-common >= %{version}-%{release}
Requires: python3-jmespath >= 0.9.0
# python-pycryptodome bundle
Provides: bundled(python-%{pycryptodome}) = %{pycryptodome_version}
# python-aliyun-sdk-core bundle
Provides: bundled(python-aliyun-sdk-core) = %{aliyunsdkcore_version}
# python-aliyun-sdk-ecs bundle
Provides: bundled(python-aliyun-sdk-ecs) = %{aliyunsdkecs_version}
# python-aliyun-sdk-vpc bundle
Provides: bundled(python-aliyun-sdk-vpc) = %{aliyunsdkvpc_version}
Obsoletes: %{name} < %{version}-%{release}
%description aliyun
The fence-agents-aliyun package contains a fence agent for Alibaba Cloud (Aliyun) instances.
%files aliyun
%defattr(-,root,root,-)
# bundled libraries
%doc pycryptodome_README.rst aliyun*_README*
%license pycryptodome_LICENSE.rst
%{_sbindir}/fence_aliyun
%{_mandir}/man8/fence_aliyun.8*
# bundled libraries
/usr/lib/fence-agents/%{bundled_lib_dir}/aliyun
%endif

%package amt-ws
License: ASL 2.0
Group: System Environment/Base
Summary: Fence agent for Intel AMT (WS-Man) devices
Requires: fence-agents-common >= %{version}-%{release}
Requires: openwsman-python3
Obsoletes: %{name} < %{version}-%{release}
BuildArch: noarch
%description amt-ws
The fence-agents-amt-ws package contains a fence agent for AMT (WS-Man) devices.
%files amt-ws
%defattr(-,root,root,-)
%{_sbindir}/fence_amt_ws
%{_mandir}/man8/fence_amt_ws.8*

%package apc
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for APC devices
Requires: openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
%if (0%{?rhel} && 0%{?rhel} < 8) || (0%{?centos} && 0%{?centos} < 8)
Requires: telnet
%else
Recommends: telnet
%endif
%endif
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: %{name} < %{version}-%{release}
BuildArch: noarch
%description apc
Fence agent for APC devices that are accessed via telnet or SSH.
%files apc
%{_sbindir}/fence_apc
%{_mandir}/man8/fence_apc.8*

%package apc-snmp
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agents for APC devices (SNMP)
Requires: net-snmp-utils
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: %{name} < %{version}-%{release}
BuildArch: noarch
%description apc-snmp
Fence agents for APC devices that are accessed via the SNMP protocol.
%files apc-snmp
%{_sbindir}/fence_apc_snmp
%{_mandir}/man8/fence_apc_snmp.8*

%ifarch x86_64
%package aws
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for Amazon AWS
Requires: fence-agents-common >= %{version}-%{release}
Requires: python3-boto3
Provides: bundled(python3-%{botocore}) = %{botocore_version}
Provides: bundled(python3-%{urllib3}) = %{urllib3_version}
Provides: bundled(python3-%{requests}) = %{requests_version}
Provides: bundled(python3-%{certifi}) = %{certifi_version}
Provides: bundled(python3-%{chrstnormalizer}) = %{chrstnormalizer_version}
Provides: bundled(python3-%{idna}) = %{idna_version}
Provides: bundled(python3-%{chardet}) = %{chardet_version}
Provides: bundled(python3-%{dateutil}) = %{dateutil_version}
Provides: bundled(python3-%{six}) = %{six_version}
Provides: bundled(python3-%{jmespath}) = %{jmespath_version}
Obsoletes: %{name} < %{version}-%{release}
BuildArch: noarch
%description aws
Fence agent for Amazon AWS instances.
%files aws
%{_sbindir}/fence_aws
%{_mandir}/man8/fence_aws.8*
# bundled libraries
/usr/lib/fence-agents/%{bundled_lib_dir}/aws
%endif

%ifarch x86_64
%package azure-arm
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for Azure Resource Manager
Requires: fence-agents-common >= %{version}-%{release}
Requires: python3-azure-sdk >= 4.0.0-9
Obsoletes: %{name} < %{version}-%{release}
BuildArch: noarch
%description azure-arm
Fence agent for Azure Resource Manager instances.
%files azure-arm
%{_sbindir}/fence_azure_arm
%{_datadir}/fence/azure_fence.py*
%{_datadir}/fence/__pycache__/azure_fence.*
%{_mandir}/man8/fence_azure_arm.8*
%endif

%package bladecenter
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for IBM BladeCenter
Requires: openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
%if (0%{?rhel} && 0%{?rhel} < 8) || (0%{?centos} && 0%{?centos} < 8)
Requires: telnet
%else
Recommends: telnet
%endif
%endif
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: %{name} < %{version}-%{release}
BuildArch: noarch
%description bladecenter
Fence agent for IBM BladeCenter devices that are accessed
via telnet or SSH.
%files bladecenter
%{_sbindir}/fence_bladecenter
%{_mandir}/man8/fence_bladecenter.8*

%package brocade
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for Brocade switches
Requires: openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
%if (0%{?rhel} && 0%{?rhel} < 8) || (0%{?centos} && 0%{?centos} < 8)
Requires: telnet
%else
Recommends: telnet
%endif
%endif
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: %{name} < %{version}-%{release}
BuildArch: noarch
%description brocade
Fence agent for Brocade devices that are accessed via telnet or SSH.
%files brocade
%{_sbindir}/fence_brocade
%{_mandir}/man8/fence_brocade.8*

%package cisco-mds
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for Cisco MDS 9000 series
Requires: net-snmp-utils
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: %{name} < %{version}-%{release}
BuildArch: noarch
%description cisco-mds
Fence agent for Cisco MDS 9000 series devices that are accessed
via the SNMP protocol.
%files cisco-mds
%{_sbindir}/fence_cisco_mds
%{_mandir}/man8/fence_cisco_mds.8*

%package cisco-ucs
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for Cisco UCS series
Requires: python3-pycurl
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: %{name} < %{version}-%{release}
BuildArch: noarch
%description cisco-ucs
Fence agent for Cisco UCS series devices that are accessed
via the SNMP protocol.
%files cisco-ucs
%{_sbindir}/fence_cisco_ucs
%{_mandir}/man8/fence_cisco_ucs.8*

%package compute
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for Nova compute nodes
Requires: python3-requests
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: %{name} < %{version}-%{release}
BuildArch: noarch
%description compute
Fence agent for Nova compute nodes.
%files compute
%{_sbindir}/fence_compute
%{_sbindir}/fence_evacuate
%{_mandir}/man8/fence_compute.8*
%{_mandir}/man8/fence_evacuate.8*

%package drac5
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for Dell DRAC 5
Requires: openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
%if (0%{?rhel} && 0%{?rhel} < 8) || (0%{?centos} && 0%{?centos} < 8)
Requires: telnet
%else
Recommends: telnet
%endif
%endif
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: %{name} < %{version}-%{release}
BuildArch: noarch
%description drac5
Fence agent for Dell DRAC 5 series devices that are accessed
via telnet or SSH.
%files drac5
%{_sbindir}/fence_drac5
%{_mandir}/man8/fence_drac5.8*

%package eaton-snmp
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for Eaton network power switches
Requires: net-snmp-utils
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: %{name} < %{version}-%{release}
BuildArch: noarch
%description eaton-snmp
Fence agent for Eaton network power switches that are accessed
via the SNMP protocol.
%files eaton-snmp
%{_sbindir}/fence_eaton_snmp
%{_mandir}/man8/fence_eaton_snmp.8*

%package emerson
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for Emerson devices (SNMP)
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: %{name} < %{version}-%{release}
BuildArch: noarch
%description emerson
Fence agent for Emerson devices that are accessed via
the SNMP protocol.
%files emerson
%{_sbindir}/fence_emerson
%{_mandir}/man8/fence_emerson.8*

%package eps
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for ePowerSwitch 8M+ power switches
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: %{name} < %{version}-%{release}
BuildArch: noarch
%description eps
Fence agent for ePowerSwitch 8M+ power switches that are accessed
via the HTTP(s) protocol.
%files eps
%{_sbindir}/fence_eps
%{_mandir}/man8/fence_eps.8*

%ifarch x86_64
%package gce
License: GPLv2+ and LGPLv2+ and MIT
Group: System Environment/Base
Summary: Fence agent for GCE (Google Cloud Engine)
Requires: fence-agents-common >= %{version}-%{release}
Requires: python3-google-api-client
Requires: python3-pysocks
# google cloud
Provides: bundled(python-httplib2) = %{httplib2_version}
Obsoletes: %{name} < %{version}-%{release}
BuildArch: noarch
%description gce
Fence agent for GCE (Google Cloud Engine) instances.
%files gce
%{_sbindir}/fence_gce
%{_mandir}/man8/fence_gce.8*
# bundled libraries
/usr/lib/fence-agents/%{bundled_lib_dir}/google
%endif

%package heuristics-ping
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Pseudo fence agent to affect other agents based on ping-heuristics
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: %{name} < %{version}-%{release}
BuildArch: noarch
%description heuristics-ping
Fence pseudo agent used to affect other agents based on
ping-heuristics.
%files heuristics-ping
%{_sbindir}/fence_heuristics_ping
%{_mandir}/man8/fence_heuristics_ping.8*

%package hpblade
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for HP BladeSystem devices
Requires: openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
%if (0%{?rhel} && 0%{?rhel} < 8) || (0%{?centos} && 0%{?centos} < 8)
Requires: telnet
%else
Recommends: telnet
%endif
%endif
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: %{name} < %{version}-%{release}
BuildArch: noarch
%description hpblade
Fence agent for HP BladeSystem devices that are accessed via telnet
or SSH.
%files hpblade
%{_sbindir}/fence_hpblade
%{_mandir}/man8/fence_hpblade.8*

%package ibmblade
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for IBM BladeCenter
Requires: net-snmp-utils
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: %{name} < %{version}-%{release}
BuildArch: noarch
%description ibmblade
Fence agent for IBM BladeCenter devices that are accessed
via the SNMP protocol.
%files ibmblade
%{_sbindir}/fence_ibmblade
%{_mandir}/man8/fence_ibmblade.8*

%package ibm-powervs
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for IBM PowerVS
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description ibm-powervs
Fence agent for IBM PowerVS that are accessed via REST API.
%files ibm-powervs
%{_sbindir}/fence_ibm_powervs
%{_mandir}/man8/fence_ibm_powervs.8*

%package ibm-vpc
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for IBM Cloud VPC
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description ibm-vpc
Fence agent for IBM Cloud VPC that are accessed via REST API.
%files ibm-vpc
%{_sbindir}/fence_ibm_vpc
%{_mandir}/man8/fence_ibm_vpc.8*

%package ifmib
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for devices with IF-MIB interfaces
Requires: net-snmp-utils
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: %{name} < %{version}-%{release}
BuildArch: noarch
%description ifmib
Fence agent for IF-MIB interfaces that are accessed via
the SNMP protocol.
%files ifmib
%{_sbindir}/fence_ifmib
%{_mandir}/man8/fence_ifmib.8*

%package ilo2
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agents for HP iLO2 devices
Requires: gnutls-utils
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: %{name} < %{version}-%{release}
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
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for HP iLO Moonshot devices
Requires: openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
%if (0%{?rhel} && 0%{?rhel} < 8) || (0%{?centos} && 0%{?centos} < 8)
Requires: telnet
%else
Recommends: telnet
%endif
%endif
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: %{name} < %{version}-%{release}
BuildArch: noarch
%description ilo-moonshot
Fence agent for HP iLO Moonshot devices that are accessed
via telnet or SSH.
%files ilo-moonshot
%{_sbindir}/fence_ilo_moonshot
%{_mandir}/man8/fence_ilo_moonshot.8*

%package ilo-mp
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for HP iLO MP devices
Requires: openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
%if (0%{?rhel} && 0%{?rhel} < 8) || (0%{?centos} && 0%{?centos} < 8)
Requires: telnet
%else
Recommends: telnet
%endif
%endif
Requires: fence-agents-common = %{version}-%{release}
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: %{name} < %{version}-%{release}
BuildArch: noarch
%description ilo-mp
Fence agent for HP iLO MP devices that are accessed via telnet or SSH.
%files ilo-mp
%{_sbindir}/fence_ilo_mp
%{_mandir}/man8/fence_ilo_mp.8*

%package ilo-ssh
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agents for HP iLO devices over SSH
Requires: openssh-clients
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: %{name} < %{version}-%{release}
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
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for devices with Intel Modular interfaces
Requires: net-snmp-utils
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: %{name} < %{version}-%{release}
BuildArch: noarch
%description intelmodular
Fence agent for Intel Modular interfaces that are accessed
via the SNMP protocol.
%files intelmodular
%{_sbindir}/fence_intelmodular
%{_mandir}/man8/fence_intelmodular.8*

%package ipdu
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for IBM iPDU network power switches
Requires: net-snmp-utils
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: %{name} < %{version}-%{release}
BuildArch: noarch
%description ipdu
Fence agent for IBM iPDU network power switches that are accessed
via the SNMP protocol.
%files ipdu
%{_sbindir}/fence_ipdu
%{_mandir}/man8/fence_ipdu.8*

%package ipmilan
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agents for devices with IPMI interface
Requires: /usr/bin/ipmitool
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: %{name} < %{version}-%{release}
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
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for use with kdump crash recovery service
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: %{name} < %{version}-%{release}
# this cannot be noarch since it's compiled
%description kdump
Fence agent for use with kdump crash recovery service.
%files kdump
%{_sbindir}/fence_kdump
%{_libexecdir}/fence_kdump_send
%{_mandir}/man8/fence_kdump.8*
%{_mandir}/man8/fence_kdump_send.8*

%package kubevirt
License: GPLv2+ and LGPLv2+ and ASL 2.0 and BSD and BSD-2-Clause and BSD-3-Clause and ISC and MIT and MPL-2.0
Summary: Fence agent for KubeVirt platform
Requires: fence-agents-common = %{version}-%{release}
Provides: bundled(python3-%{openshift}) = %{openshift_version}
Provides: bundled(python3-%{ruamelyamlclib}) = %{ruamelyamlclib_version}
Provides: bundled(python3-%{kubernetes}) = %{kubernetes_version}
Provides: bundled(python3-%{certifi}) = %{certifi_version}
Provides: bundled(python3-%{googleauth}) = %{googleauth_version}
Provides: bundled(python3-%{cachetools}) = %{cachetools_version}
Provides: bundled(python3-%{pyasn1modules}) = %{pyasn1modules_version}
Provides: bundled(python3-%{pyasn1}) = %{pyasn1_version}
Provides: bundled(python3-%{dateutil}) = %{dateutil_version}
Provides: bundled(python3-%{pyyaml}) = %{pyyaml_version}
Provides: bundled(python3-%{six}) = %{six_version}
Provides: bundled(python3-%{urllib3}) = %{urllib3_version}
Provides: bundled(python3-%{websocketclient}) = %{websocketclient_version}
Provides: bundled(python3-%{jinja2}) = %{jinja2_version}
Provides: bundled(python3-%{markupsafe}) = %{markupsafe_version}
Provides: bundled(python3-%{stringutils}) = %{stringutils_version}
Provides: bundled(python3-%{requests}) = %{requests_version}
Provides: bundled(python3-%{chrstnormalizer}) = %{chrstnormalizer_version}
Provides: bundled(python3-%{idna}) = %{idna_version}
Provides: bundled(python3-%{reqstsoauthlib}) = %{reqstsoauthlib_version}
Provides: bundled(python3-%{oauthlib}) = %{oauthlib_version}
Provides: bundled(python3-%{ruamelyaml}) = %{ruamelyaml_version}
Provides: bundled(python3-%{setuptools}) = %{setuptools_version}
%description kubevirt
Fence agent for KubeVirt platform.
%files kubevirt
%{_sbindir}/fence_kubevirt
%{_mandir}/man8/fence_kubevirt.8*
# bundled libraries
/usr/lib/fence-agents/%{bundled_lib_dir}/kubevirt

%package lpar
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for IBM LPAR
Requires: openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
%if (0%{?rhel} && 0%{?rhel} < 8) || (0%{?centos} && 0%{?centos} < 8)
Requires: telnet
%else
Recommends: telnet
%endif
%endif
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: %{name} < %{version}-%{release}
BuildArch: noarch
%description lpar
Fence agent for IBM LPAR devices that are accessed via telnet or SSH.
%files lpar
%{_sbindir}/fence_lpar
%{_mandir}/man8/fence_lpar.8*

%package mpath
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for reservations over Device Mapper Multipath
Requires: device-mapper-multipath
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: %{name} < %{version}-%{release}
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
License: GPLv2+ and LGPLv2+ and ASL 2.0 and MIT and Python
Summary: Fence agent for OpenStack's Nova service
%if 0%{?fedora} || 0%{?centos} > 7 || 0%{?rhel} > 7 || 0%{?suse_version}
Requires: python3-requests
%else
Requires: python-requests
%endif
Requires: fence-agents-common = %{version}-%{release}
%description openstack
Fence agent for OpenStack's Nova service.
%files openstack
%{_sbindir}/fence_openstack
%{_mandir}/man8/fence_openstack.8*
%endif

%package redfish
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for Redfish
Requires: fence-agents-common >= %{version}-%{release}
Requires: python3-requests
Obsoletes: %{name} < %{version}-%{release}
%description redfish
The fence-agents-redfish package contains a fence agent for Redfish
%files redfish
%defattr(-,root,root,-)
%{_sbindir}/fence_redfish
%{_mandir}/man8/fence_redfish.8*

%package rhevm
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for RHEV-M
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: %{name} < %{version}-%{release}
BuildArch: noarch
%description rhevm
Fence agent for RHEV-M via REST API.
%files rhevm
%{_sbindir}/fence_rhevm
%{_mandir}/man8/fence_rhevm.8*

%if 0%{?fedora} || 0%{?rhel} > 7
%package rsa
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for IBM RSA II
Requires: openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
%if (0%{?rhel} && 0%{?rhel} < 8) || (0%{?centos} && 0%{?centos} < 8)
Requires: telnet
%else
Recommends: telnet
%endif
%endif
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: %{name} < %{version}-%{release}
BuildArch: noarch
%description rsa
Fence agent for IBM RSA II devices that are accessed
via telnet or SSH.
%files rsa
%{_sbindir}/fence_rsa
%{_mandir}/man8/fence_rsa.8*
%endif

%package rsb
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for Fujitsu RSB
Requires: openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
%if (0%{?rhel} && 0%{?rhel} < 8) || (0%{?centos} && 0%{?centos} < 8)
Requires: telnet
%else
Recommends: telnet
%endif
%endif
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: %{name} < %{version}-%{release}
BuildArch: noarch
%description rsb
Fence agent for Fujitsu RSB devices that are accessed
via telnet or SSH.
%files rsb
%{_sbindir}/fence_rsb
%{_mandir}/man8/fence_rsb.8*

%if 0%{?fedora} || 0%{?rhel} > 7
%package sbd
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for SBD (storage-based death)
Requires: sbd
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: %{name} < %{version}-%{release}
BuildArch: noarch
%description sbd
Fence agent for SBD (storage-based death).
%files sbd
%{_sbindir}/fence_sbd
%{_mandir}/man8/fence_sbd.8*
%endif

%package scsi
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for SCSI persistent reservations
Requires: sg3_utils
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: %{name} < %{version}-%{release}
BuildArch: noarch
%description scsi
Fence agent for SCSI persistent reservations.
%files scsi
%{_sbindir}/fence_scsi
%{_datadir}/cluster/fence_scsi_check
%{_datadir}/cluster/fence_scsi_check_hardreboot
%{_mandir}/man8/fence_scsi.8*

%package virsh
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for virtual machines based on libvirt
Requires: openssh-clients /usr/bin/virsh
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: %{name} < %{version}-%{release}
BuildArch: noarch
%description virsh
Fence agent for virtual machines that are accessed via SSH.
%files virsh
%{_sbindir}/fence_virsh
%{_mandir}/man8/fence_virsh.8*

%package vmware-rest
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for VMWare with REST API
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: %{name} < %{version}-%{release}
BuildArch: noarch
%description vmware-rest
Fence agent for VMWare with REST API.
%files vmware-rest
%{_sbindir}/fence_vmware_rest
%{_mandir}/man8/fence_vmware_rest.8*

%package vmware-soap
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for VMWare with SOAP API v4.1+
Requires: python3-suds python3-requests
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: %{name} < %{version}-%{release}
BuildArch: noarch
%description vmware-soap
Fence agent for VMWare with SOAP API v4.1+.
%files vmware-soap
%{_sbindir}/fence_vmware_soap
%{_mandir}/man8/fence_vmware_soap.8*

%package wti
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for WTI Network power switches
Requires: openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
%if (0%{?rhel} && 0%{?rhel} < 8) || (0%{?centos} && 0%{?centos} < 8)
Requires: telnet
%else
Recommends: telnet
%endif
%endif
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: %{name} < %{version}-%{release}
BuildArch: noarch
%description wti
Fence agent for WTI network power switches that are accessed
via telnet or SSH.
%files wti
%{_sbindir}/fence_wti
%{_mandir}/man8/fence_wti.8*

%ifarch s390x
%package zvm
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for IBM z/VM over IP
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: %{name} < %{version}-%{release}
BuildArch: noarch
%description zvm
Fence agent for IBM z/VM over IP.
%files zvm
%{_sbindir}/fence_zvmip
%{_mandir}/man8/fence_zvmip.8*
%endif

%changelog
* Thu Aug  3 2023 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-121
- bundled dateutil: fix tarfile CVE-2007-4559
  Resolves: rhbz#2218234

* Tue Jul 11 2023 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-119
- fence_ibm_powervs: performance improvements
  Resolves: rhbz#2155453

* Mon Jul  3 2023 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-118
- fence_azure_arm: add Stack Hub support
  Resolves: rhbz#2211460

* Thu May  4 2023 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-115
- fence_scsi: detect devices in shared VGs
  Resolves: rhbz#2187329

* Wed May  3 2023 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-114
- fence_aws: add --skip-race-check parameter to allow running outside
  of AWS network
  Resolves: rhbz#2183158

* Thu Jan 26 2023 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-112
- fence_vmware_soap: set login_timeout lower than default
  pcmk_monitor_timeout (20s) to remove tmp dirs
  Resolves: rhbz#1787178

* Wed Jan 25 2023 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-111
- fencing/fence_wti: add --plug-separator to be able to avoid
  characters that are in node name(s)
  Resolves: rhbz#2152105

* Fri Jan 13 2023 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-110
- fence_scsi: skip key generation during validate-all action
  Resolves: rhbz#2160478

* Thu Oct 27 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-108
- fence_ibm_powervs: improve defaults
  Resolves: rhbz#2136076

* Wed Oct 12 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-107
- fence_lpar: only output additional output info on DEBUG level
  Resolves: rhbz#2134017

* Mon Sep  5 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-106
- fence_ibm_vpc: add token cache support
  Resolves: rhbz#2102024

* Tue Aug 16 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-103
- fence_openstack: new fence agent
  Resolves: rhbz#1886074

* Wed Jun 22 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-99
- fence_ibm_powervs: add support for proxy, private API servers and
  get token via API key
  Resolves: rhbz#2092921

* Tue Jun  7 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-98
- fence_ibm_vpc: add proxy support
  Resolves: rhbz#2091826

* Tue May 31 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-96
- all agents: unify ssl parameters to avoid having to use --ssl when
  using --ssl-secure/--ssl-insecure for some agents
  Resolves: rhbz#2072421

* Tue May 17 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-95
- fence_apc/fence_ilo_moonshot/fence_lpar: add missing "import logging"
  Resolves: rhbz#2080729

* Thu May  5 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-94
- fence_ibm_vpc: remove unused instance parameter and make limit
  optional
  Resolves: rhbz#2080994

* Thu Apr 28 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-93
- fence_gce: update fence agent
  Resolves: rhbz#2078244

* Wed Apr 27 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-92
- fence_ibm_vpc: new fence agent
  Resolves: rhbz#1728203

* Fri Feb 11 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-88
- fence_aws: upgrade botocore to fix IMDSv2 support
  Resolves: rhbz#2048857

* Wed Jan 19 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-85
- fence_ibm_powervs: new fence agent
  Resolves: rhbz#1874862

* Mon Jan 17 2022 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-84
- fence_kubevirt: new fence agent
  Resolves: rhbz#1977588

* Thu Nov 11 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-83
- fence_zvmip: add SSL/TLS support
  Resolves: rhbz#1963163

* Tue Nov  2 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-80
- fence_sbd: dont spam logs when disable_timeout is enabled
  Resolves: rhbz#1971683

* Wed Oct 27 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-79
- fence_amt_ws: fix "or" causing dead code
  Resolves: rhbz#2010710
- fence_gce: add proxy support
  Resolves: rhbz#1969953

* Tue Oct 19 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-78
- all agents: log exceptions when failing
  Resolves: rhbz#1470827

* Wed Aug 11 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-75
- fence_gce: add serviceaccount JSON file support
  Resolves: rhbz#1685814

* Thu May 20 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-72
- fence_mpath: add watchdog retry support
  Resolves: rhbz#1922437

* Fri May  7 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-71
- fence_redfish: add diag action
  Resolves: rhbz#1920947

* Thu May  6 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-70
- fence_gce: change default back to cycle to avoid "soft" off
  Resolves: rhbz#1942363

* Tue May  4 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-69
- fencing: add "stonith_status_sleep" parameter to set sleep between
  status calls during STONITH action
  Resolves: rhbz#1780825

* Fri Apr 30 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-68
- fence_aws: add "filter" parameter
  Resolves: rhbz#1941989

* Wed Mar  3 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-67
- fence_ipmilanplus: new symlink agent with lanplus enabled by default
  Resolves: rhbz#1925015

* Tue Feb  2 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-65
- fence_gce: default to onoff
  Resolves: rhbz#1906978

* Mon Jan 11 2021 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-63
- fence_zvmip: fix disable-timeout not working correctly
  Resolves: rhbz#1914313

* Fri Nov 13 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-62
- fence_aws: add support for IMDSv2
  Resolves: rhbz#1896827

* Tue Nov 10 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-61
- fence_scsi: dont write key to device if it's already registered,
  and dont write device to file when cluster is started again
  Resolves: rhbz#1841087

* Thu Nov  5 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-59
- fencing: add disable-timeout parameter and make it true by default
  for Pacemaker 2.0+
  Resolves: rhbz#1470813, rhbz#1436429

* Mon Sep 14 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-54
- fence_azure_arm: fix MSI support
  Resolves: rhbz#1818157
- fence_mpath: allow spaces for comma-separated devices and add
  support for space-separated devices
  Resolves: rhbz#1851115
- fence_ipmilan: add ability to increase ipmitool verbosity
  Resolves: rhbz#1853973
- fence_lpar: fix list-status action
  Resolves: rhbz#1861926
- all agents: make telnet a weak dependency
  Resolves: rhbz#1851232

* Fri Aug  7 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-53
- fence_evacuate: enable evacuation of instances using private flavors
  Resolves: rhbz#1859932

* Tue Jul 28 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-52
- fence_lpar: fix issue with long username, hostname, etc not
  working when the command run by the agent exceeds 80 characters
  Resolves: rhbz#1860544

* Thu Jul  2 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-51
- fence_vmware_rest: fix encoding issues
  Resolves: rhbz#1793739

* Thu Jun 11 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-50
- fence_vmware_soap: log exception message for SSLError exception
  Resolves: rhbz#1796654

* Wed May 27 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-49
- fence_aws: improve logging by catching ConnectionError exception
  Resolves: rhbz#1839776

* Fri May 15 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-47
- fence_vmware_rest: add filter parameter to avoid 1000 VM API limit
  and avoid failing when hitting it during the monitor-action
  Resolves: rhbz#1827652
- fence_compute/fence_evacuate: fix --insecure parameter
  Resolves: rhbz#1830776
- fence_scsi: add readonly parameter
  Resolves: rhbz#1750596

* Tue Apr 28 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-45
- fence_vmware_rest: improve exception handling
  Resolves: rhbz#1827559

* Tue Mar 24 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-44
- fence_aws: fix possible race condition

  Resolves: rhbz#1816203

* Fri Mar 13 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-42
- fence-agents-lpar: build on non-ppc64le arch's
  Resolves: rhbz#1804907
- fence_aws: improve parameter logic to allow setting region parameter
  while using credentials from ~/.aws/config
  Resolves: rhbz#1810457

* Thu Feb 13 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-41
- fence_mpath: add plug parameter support to be able to use pcmk_host_map
  Resolves: rhbz#1753228
- fence_mpath: fix --reserve parameter typo
  Resolves: rhbz#1798641

* Fri Jan 31 2020 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-40
- fence_aws: improve logging and metadata/usage text
  Resolves: rhbz#1781357

* Tue Nov 26 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-39
- fencing: only use inetX_only parameters for SSH based agents and
  fence_zvmip
  Resolves: rhbz#1771594

* Wed Nov 20 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-38
- fence_sbd: add stderr support
  Resolves: rhbz#1774458

* Tue Nov 19 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-37
- fence_scsi: add hash key-value support
  Resolves: rhbz#1773890

* Wed Nov 13 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-35
- fence_rhevm: add cookie support
  Resolves: rhbz#1763674

* Thu Nov  7 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-34
- fence_compute/fence_evacuate: fix region_name content type and
  project shortopt in usage text and project-domain shortopt
  Resolves: rhbz#1760201
- fencing: improve stdin quote parsing
  Resolves: rhbz#1769783

* Fri Oct 18 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-33
- fence_vmware_rest: improve logging
  Resolves: rhbz#1760224

* Wed Oct 16 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-32
- fence_compute: disable service after force-down
  Resolves: rhbz#1760213

* Thu Oct  3 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-31
- fence_aliyun: add RAM role support
  Resolves: rhbz#1732766
- fence_ilo4_ssh/fence_ilo5_ssh: add monitor timeout warning
  Resolves: rhbz#1734811
- fence_mpath: fix watchdog reboot not triggered when multipath
  disconnected
  Resolves: rhbz#1751704

* Fri Sep  6 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-30
- fence_zvmip: fix Python 3 issues
  Resolves: rhbz#1748443

* Thu Jul 25 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-29
- fence_vmware_rest: fix KeyError issue for suspended VMs
  Resolves: rhbz#1732773

* Wed Jul 24 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-28
- fence_mpath: fix watchdog hardreboot
  Resolves: rhbz#1709926

* Thu Jun 13 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-27
- fence_scsi watchdog: fix failing on first try when using retry
  Resolves: rhbz#1720198

* Tue May 28 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-25
- fence_redfish: add header for full Redfish spec compliance
  Resolves: rhbz#1704228
- fence_scsi: fix to match new node ID format
  Resolves: rhbz#1714458

* Thu May 23 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-24
- fence_azure_arm: use skip_shutdown feature
  Resolves: rhbz#1700546

* Tue May 21 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-23
- fence_rhevm: add RHEV v4 API support and auto-detection
  Resolves: rhbz#1709780
- fence_rhevm: fix encoding issues
  Resolves: rhbz#1712263

* Fri Apr  5 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-22
- fence_gce: fix Python 3 encoding issue
  Resolves: rhbz#1696584

* Mon Apr  1 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-21
- Add CI gating tests
  Resolves: rhbz#1682125

* Fri Mar 22 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-20
- fence_aliyun: upgrade python-aliyun-sdk-core to fix httplib issue
  Resolves: rhbz#1677945

* Tue Mar 19 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-18
- fence_redfish: use ipport parameter
  Resolves: rhbz#1677327

* Fri Feb  8 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-17
- fence-agents-vmware-soap: add missing python3-requests dependency
  Resolves: rhbz#1591502

* Mon Jan 28 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-16
- fence_redfish: new fence agent
  Resolves: rhbz#1666914

* Fri Jan 25 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-13
- fence-agents-scsi: add missing fence-agents-common dependency
  Resolves: rhbz#1665170
- fence_azure_arm: add bundled directory to search path
  Resolves: rhbz#1650214

* Fri Dec  7 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-11
- fence_scsi: fix incorrect SCSI-key when node ID is 10 or higher
  Resolves: rhbz#1654968
- fence_scsi: add watchdog retry support
  Resolves: rhbz#1654976
- fence_hpblade: fix log_expect syntax
  Resolves: rhbz#1654616
- fence_vmware_soap: cleanup when receiving SIGTERM
  Resolves: rhbz#1654973

* Mon Oct  8 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-10
- spec-file improvements by Jan Pokorny
- fence_aliyun: bundled libraries
  Resolves: rhbz#1625208

* Tue Aug 14 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-7
- fence_kdump: fix strncpy issue

* Wed Jul 11 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-6
- fence_evacuate: fix evacuable tag mix issue

* Wed Jul  4 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-5
- Use %{__python3} macro to set correct Python #!

* Mon Jun 18 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-4
- fence_vmware_soap: fix python3-suds issue
- Remove unsupported agents

* Mon Jun 11 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-2
- Remove fence-agents-amt due to missing amtterm

* Thu May 31 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-1
- new upstream release

* Thu May 17 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.0-1
- new upstream release

* Thu Feb 15 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.1-1
- new upstream release
- fence_vmware_soap / fence_ovh: use Python 2 till python3-suds bug
  is fixed

* Fri Feb  9 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.1.0-2
- new upstream release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.24-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Iryna Shcherbina <ishcherb@redhat.com> - 4.0.24-14
- Cleanup no longer needed Python 2 dependencies

* Tue Nov 07 2017 Troy Dawson <tdawson@redhat.com> - 4.0.24-13
- Cleanup spec file conditionals

* Tue Aug 29 2017 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.24-12
- fence-agents-common: remove fence_scsi_check files
- fence-scsi: add "fence_scsi_check_hardreboot"

* Thu Aug  3 2017 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.24-10
- fence_zvm: fix "uintptr_t" undeclared

* Thu Aug  3 2017 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.24-9
- Fix encoding for pexpect with Python 3.6

  Resolves: rhbz#1473908

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.24-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.24-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.24-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 23 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.24-5
- Fix to build in Python 3 only environment

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 4.0.24-4
- Rebuild for Python 3.6

* Wed Sep 21 2016 Marek Grac <mgrac@redhat.com> - 4.0.24-4
- Remove Obsoletes that are no longer valid

* Fri Sep  2 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.24-2
- fence-agents-common: add dependency on python3-pycurl

* Fri Aug 26 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.24-1
- new upstream release

* Wed Jul 13 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.23-2
- fix build issue on s390

* Tue Jul 12 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.23-1
- new upstream release
- new package fence-agents-amt-ws
- new package fence-agents-compute
- new package fence-agents-drac
- new package fence-agents-hds-cb
- new package fence-agents-mpath
- new package fence-agents-sanbox2
- new package fence-agents-sbd
- new package fence-agents-vbox
- new package fence-agents-vmware
- new package fence-agents-xenapi

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Aug 11 2015 Marek Grac <mgrac@redhat.com> - 4.0.20-1
- new upstream release
- new package fence-agents-rcd-serial

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 05 2015 Marek Grac <mgrac@redhat.com> - 4.0.16-1
- new upstream release

* Mon Feb 09 2015 Marek Grac <mgrac@redhat.com> - 4.0.15-1
- new upstream release

* Thu Jan 08 2015 Marek Grac <mgrac@redhat.com> - 4.0.14-1
- new upstream release
- new packages fence-agents-zvm and fence-agents-emerson

* Thu Oct 16 2014 Marek Grac <mgrac@redhat.com> - 4.0.12-1
- new upstream release
- new package fence-agents-ilo-ssh

* Wed Aug 27 2014 Marek Grac <mgrac@redhat.com> - 4.0.10
- new upstream release
- new package fence-agents-ilo-moonshot

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 16 2014 Marek Grac <mgrac@redhat.com> - 4.0.9
- new upstream release
- new package fence-agents-pve

* Mon Apr 07 2014 Marek Grac <mgrac@redhat.com> - 4.0.8-1
- new upstream release
- new package fence-agents-raritan

* Wed Feb 26 2014 Marek Grac <mgrac@redhat.com> - 4.0.7-3
- requires a specific version of fence-agents-common

* Mon Feb 17 2014 Marek Grac <mgrac@redhat.com> - 4.0.7-2
- new upstream release
- changed dependancy from nss/nspr to gnutls-utils

* Fri Jan 10 2014 Marek Grac <mgrac@redhat.com> - 4.0.4-4
- new upstream release
- new package fence-agents-amt

* Mon Oct 07 2013 Marek Grac <mgrac@redhat.com> - 4.0.4-3
- new upstream release
- new package fence-agents-netio

* Tue Sep 03 2013 Marek Grac <mgrac@redhat.com> - 4.0.3-1
- new upstream release
- new packages fence-agents-brocade and fence-agents-ovh

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 4.0.1-2
- Perl 5.18 rebuild

* Mon Jul 01 2013 Marek Grac <mgrac@redhat.com> - 4.0.1-1
- new upstream release

* Mon Jun 24 2013 Marek Grac <mgrac@redhat.com> - 4.0.0-5
- fence-agents-all should provide fence-agent for clean update path

* Wed Apr 03 2013 Marek Grac <mgrac@redhat.com> - 4.0.0-4
- minor changes in spec file

* Thu Mar 21 2013 Marek Grac <mgrac@redhat.com> - 4.0.0-3
- minor changes in spec file

* Mon Mar 18 2013 Marek Grac <mgrac@redhat.com> - 4.0.0-2
- minor changes in spec file

* Mon Mar 11 2013 Marek Grac <mgrac@redhat.com> - 4.0.0-1
- new upstream release
- introducing subpackages


