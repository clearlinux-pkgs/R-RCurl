#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-RCurl
Version  : 1.95.4.8
Release  : 38
URL      : http://cran.r-project.org/src/contrib/RCurl_1.95-4.8.tar.gz
Source0  : http://cran.r-project.org/src/contrib/RCurl_1.95-4.8.tar.gz
Summary  : General Network (HTTP/FTP/...) Client Interface for R
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: R-RCurl-lib
Requires: R-bitops
BuildRequires : R-bitops
BuildRequires : clr-R-helpers
BuildRequires : curl-dev
BuildRequires : libidn-dev
BuildRequires : libxml2-dev
BuildRequires : nghttp2-dev
BuildRequires : openssl-dev
BuildRequires : xz-dev
BuildRequires : zlib-dev

%description
This package is a (currently) simple interface to the
libcurl functionality.  This is an extensive and well
tested library that takes care of so many details that
we would have to mimic (probably incompletely and poorly)
if we were to write this in the R language directly.

%package lib
Summary: lib components for the R-RCurl package.
Group: Libraries

%description lib
lib components for the R-RCurl package.


%prep
%setup -q -c -n RCurl

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1492801688

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1492801688
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RCurl
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library RCurl || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/RCurl/CurlSSL/boost.pem
/usr/lib64/R/library/RCurl/CurlSSL/ca-bundle.crt
/usr/lib64/R/library/RCurl/CurlSSL/cacert.pem
/usr/lib64/R/library/RCurl/CurlSSL/certs
/usr/lib64/R/library/RCurl/CurlSSL/certs.pem
/usr/lib64/R/library/RCurl/CurlSSL/curlSSL.xml
/usr/lib64/R/library/RCurl/CurlSSL/cybertrust.pem
/usr/lib64/R/library/RCurl/CurlSSL/docs
/usr/lib64/R/library/RCurl/CurlSSL/google.pem
/usr/lib64/R/library/RCurl/CurlSSL/myBundle.crt
/usr/lib64/R/library/RCurl/CurlSSL/ok.R
/usr/lib64/R/library/RCurl/CurlSSL/server.pem
/usr/lib64/R/library/RCurl/CurlSSL/statEth.pem
/usr/lib64/R/library/RCurl/DESCRIPTION
/usr/lib64/R/library/RCurl/HTTPErrors/makeErrorClasses.R
/usr/lib64/R/library/RCurl/INDEX
/usr/lib64/R/library/RCurl/Meta/Rd.rds
/usr/lib64/R/library/RCurl/Meta/data.rds
/usr/lib64/R/library/RCurl/Meta/features.rds
/usr/lib64/R/library/RCurl/Meta/hsearch.rds
/usr/lib64/R/library/RCurl/Meta/links.rds
/usr/lib64/R/library/RCurl/Meta/nsInfo.rds
/usr/lib64/R/library/RCurl/Meta/package.rds
/usr/lib64/R/library/RCurl/NAMESPACE
/usr/lib64/R/library/RCurl/R/RCurl
/usr/lib64/R/library/RCurl/R/RCurl.rdb
/usr/lib64/R/library/RCurl/R/RCurl.rdx
/usr/lib64/R/library/RCurl/data/mimeTypeExtensions.rda
/usr/lib64/R/library/RCurl/doc/FAQ.html
/usr/lib64/R/library/RCurl/doc/cookies.xml
/usr/lib64/R/library/RCurl/doc/fileUploads.xml
/usr/lib64/R/library/RCurl/doc/philosophy.html
/usr/lib64/R/library/RCurl/doc/philosophy.xml
/usr/lib64/R/library/RCurl/doc/withCookies.Rdb
/usr/lib64/R/library/RCurl/doc/withCookies.html
/usr/lib64/R/library/RCurl/enums/Renums.c
/usr/lib64/R/library/RCurl/etc/README
/usr/lib64/R/library/RCurl/etc/ca-bundle.crt
/usr/lib64/R/library/RCurl/examples/CIS/cis.R
/usr/lib64/R/library/RCurl/examples/CIS/cis1.R
/usr/lib64/R/library/RCurl/examples/chunks.S
/usr/lib64/R/library/RCurl/examples/cis1.R
/usr/lib64/R/library/RCurl/examples/concurrent.S
/usr/lib64/R/library/RCurl/examples/concurrent.html
/usr/lib64/R/library/RCurl/examples/concurrent.xml
/usr/lib64/R/library/RCurl/examples/curl.c
/usr/lib64/R/library/RCurl/examples/download.R
/usr/lib64/R/library/RCurl/examples/elapsed.png
/usr/lib64/R/library/RCurl/examples/encoding.R
/usr/lib64/R/library/RCurl/examples/ftpList.R
/usr/lib64/R/library/RCurl/examples/getinfo.S
/usr/lib64/R/library/RCurl/examples/headers.S
/usr/lib64/R/library/RCurl/examples/headers2.S
/usr/lib64/R/library/RCurl/examples/html.S
/usr/lib64/R/library/RCurl/examples/logo.jpg
/usr/lib64/R/library/RCurl/examples/multi.S
/usr/lib64/R/library/RCurl/examples/nestedHTML.html
/usr/lib64/R/library/RCurl/examples/nestedHTML.xml
/usr/lib64/R/library/RCurl/examples/omg.netrc
/usr/lib64/R/library/RCurl/examples/passwd.S
/usr/lib64/R/library/RCurl/examples/passwd2.S
/usr/lib64/R/library/RCurl/examples/passwdSSL.S
/usr/lib64/R/library/RCurl/examples/post.c
/usr/lib64/R/library/RCurl/examples/post.html
/usr/lib64/R/library/RCurl/examples/postFormPasswd.R
/usr/lib64/R/library/RCurl/examples/progress.S
/usr/lib64/R/library/RCurl/examples/proxy.R
/usr/lib64/R/library/RCurl/examples/readHeader.S
/usr/lib64/R/library/RCurl/examples/soap.S
/usr/lib64/R/library/RCurl/examples/speakeasy.S
/usr/lib64/R/library/RCurl/examples/system.png
/usr/lib64/R/library/RCurl/examples/time.R
/usr/lib64/R/library/RCurl/examples/upload.R
/usr/lib64/R/library/RCurl/examples/user.png
/usr/lib64/R/library/RCurl/examples/worm.S
/usr/lib64/R/library/RCurl/examples/xmlParse.html
/usr/lib64/R/library/RCurl/examples/xmlParse.xml
/usr/lib64/R/library/RCurl/help/AnIndex
/usr/lib64/R/library/RCurl/help/RCurl.rdb
/usr/lib64/R/library/RCurl/help/RCurl.rdx
/usr/lib64/R/library/RCurl/help/aliases.rds
/usr/lib64/R/library/RCurl/help/paths.rds
/usr/lib64/R/library/RCurl/html/00Index.html
/usr/lib64/R/library/RCurl/html/R.css
/usr/lib64/R/library/RCurl/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/RCurl/libs/RCurl.so
