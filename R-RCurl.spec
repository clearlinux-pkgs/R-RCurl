#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-RCurl
Version  : 1.98.1.3
Release  : 84
URL      : https://cran.r-project.org/src/contrib/RCurl_1.98-1.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/RCurl_1.98-1.3.tar.gz
Summary  : General Network (HTTP/FTP/...) Client Interface for R
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: R-RCurl-lib = %{version}-%{release}
Requires: R-bitops
BuildRequires : R-bitops
BuildRequires : buildreq-R
BuildRequires : curl-dev
BuildRequires : libidn-dev
BuildRequires : libxml2-dev
BuildRequires : nghttp2-dev
BuildRequires : openssl-dev
BuildRequires : xz-dev
BuildRequires : zlib-dev

%description
Provides functions to allow one to compose general HTTP requests
        and provides convenient functions to fetch URIs, get & post
        forms, etc. and process the results returned by the Web server.
        This provides a great deal of control over the HTTP/FTP/...
        connection and the form of the request while providing a
        higher-level interface than is available just using R socket
        connections.  Additionally, the underlying implementation is
        robust and extensive, supporting FTP/FTPS/TFTP (uploads and
        downloads), SSL/HTTPS, telnet, dict, ldap, and also supports
        cookies, redirects, authentication, etc.

%package lib
Summary: lib components for the R-RCurl package.
Group: Libraries

%description lib
lib components for the R-RCurl package.


%prep
%setup -q -c -n RCurl
cd %{_builddir}/RCurl

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1615993941

%install
export SOURCE_DATE_EPOCH=1615993941
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RCurl
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RCurl
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RCurl
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc RCurl || :


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
/usr/lib64/R/library/RCurl/LICENSE
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
/usr/lib64/R/library/RCurl/doc/Changes.html
/usr/lib64/R/library/RCurl/doc/FAQ.html
/usr/lib64/R/library/RCurl/doc/cookies.xml
/usr/lib64/R/library/RCurl/doc/fileUploads.xml
/usr/lib64/R/library/RCurl/doc/getURL.html
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
/usr/lib64/R/library/RCurl/tests/dynSetReader.R
/usr/lib64/R/library/RCurl/tests/jpeg.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/RCurl/libs/RCurl.so
