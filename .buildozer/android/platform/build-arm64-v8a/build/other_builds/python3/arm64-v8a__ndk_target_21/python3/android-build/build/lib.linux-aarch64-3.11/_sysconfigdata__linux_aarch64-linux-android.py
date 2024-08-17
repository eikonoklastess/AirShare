# system configuration generated and used by the sysconfig module
build_time_vars = {'ABIFLAGS': '',
 'AC_APPLE_UNIVERSAL_BUILD': 0,
 'AIX_BUILDDATE': 0,
 'AIX_GENUINE_CPLUSPLUS': 0,
 'ALIGNOF_LONG': 8,
 'ALIGNOF_SIZE_T': 8,
 'ALT_SOABI': 0,
 'ANDROID_API_LEVEL': 21,
 'AR': '/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/bin/llvm-ar',
 'ARFLAGS': 'rcs',
 'BASECFLAGS': '',
 'BASECPPFLAGS': '-IObjects -IInclude -IPython',
 'BASEMODLIBS': '',
 'BINDIR': '/usr/local/bin',
 'BINLIBDEST': '/usr/local/lib/python3.11',
 'BLDLIBRARY': '-L. -lpython3.11',
 'BLDSHARED': '/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/bin/clang '
              '-target aarch64-linux-android21 -fomit-frame-pointer '
              '-march=armv8-a -fPIC -pthread -shared -Wl,-O1 '
              '-Wl,-Bsymbolic-functions '
              '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/libs_collections/myapp/arm64-v8a '
              '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/sqlite3/arm64-v8a__ndk_target_21/sqlite3/obj/local/arm64-v8a '
              '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/libffi/arm64-v8a__ndk_target_21/libffi/.libs '
              '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1 '
              '-L/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/lib/aarch64-linux-android/21   '
              '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/libs_collections/myapp/arm64-v8a '
              '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/sqlite3/arm64-v8a__ndk_target_21/sqlite3/obj/local/arm64-v8a '
              '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/libffi/arm64-v8a__ndk_target_21/libffi/.libs '
              '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1 '
              '-L/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/lib/aarch64-linux-android/21',
 'BOOTSTRAP_HEADERS': '\\',
 'BUILDEXE': '.exe',
 'BUILDPYTHON': 'python.exe',
 'BUILD_GNU_TYPE': 'aarch64-apple-darwin23.4.0',
 'BYTESTR_DEPS': '\\',
 'CC': '/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/bin/aarch64-linux-android21-clang',
 'CCSHARED': '',
 'CFLAGS': '-DNDEBUG -g -fwrapv -O3 -Wall -fPIC -DANDROID -fPIC -DANDROID',
 'CFLAGSFORSHARED': '',
 'CFLAGS_ALIASING': '-fno-strict-aliasing',
 'CFLAGS_NODIST': '',
 'CONFIGFILES': 'configure configure.ac acconfig.h pyconfig.h.in '
                'Makefile.pre.in',
 'CONFIGURE_CFLAGS': '-fPIC -DANDROID',
 'CONFIGURE_CFLAGS_NODIST': '-std=c11 -Werror=implicit-function-declaration '
                            '-fvisibility=hidden',
 'CONFIGURE_CPPFLAGS': '-DANDROID '
                       '-I/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/include '
                       '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/python-installs/myapp/arm64-v8a/include/python3.1 '
                       '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/sqlite3/arm64-v8a__ndk_target_21/sqlite3 '
                       '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/libffi/arm64-v8a__ndk_target_21/libffi/include '
                       '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include '
                       '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include/internal '
                       '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include/openssl '
                       '-I/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/include',
 'CONFIGURE_LDFLAGS': '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/libs_collections/myapp/arm64-v8a '
                      '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/sqlite3/arm64-v8a__ndk_target_21/sqlite3/obj/local/arm64-v8a '
                      '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/libffi/arm64-v8a__ndk_target_21/libffi/.libs '
                      '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1 '
                      '-L/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/lib/aarch64-linux-android/21',
 'CONFIGURE_LDFLAGS_NODIST': '',
 'CONFIGURE_LDFLAGS_NOLTO': '',
 'CONFIG_ARGS': "'--host=aarch64-linux-android' "
                "'--build=aarch64-apple-darwin23.4.0' '--enable-shared' "
                "'--enable-ipv6' 'ac_cv_file__dev_ptmx=yes' "
                "'ac_cv_file__dev_ptc=no' '--without-ensurepip' "
                "'ac_cv_little_endian_double=yes' "
                "'ac_cv_header_sys_eventfd_h=no' '--prefix=/usr/local' "
                "'--exec-prefix=/usr/local' "
                "'--enable-loadable-sqlite-extensions' "
                "'--with-build-python=/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/hostpython3/desktop/hostpython3/native-build/python3' "
                "'--with-openssl=/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1' "
                "'build_alias=aarch64-apple-darwin23.4.0' "
                "'host_alias=aarch64-linux-android' "
                "'PKG_CONFIG_PATH=/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/libffi/arm64-v8a__ndk_target_21/libffi' "
                "'CC=/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/bin/aarch64-linux-android21-clang' "
                "'CFLAGS=-fPIC -DANDROID' 'LDFLAGS=  "
                '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/libs_collections/myapp/arm64-v8a '
                '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/sqlite3/arm64-v8a__ndk_target_21/sqlite3/obj/local/arm64-v8a '
                '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/libffi/arm64-v8a__ndk_target_21/libffi/.libs '
                '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1 '
                "-L/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/lib/aarch64-linux-android/21' "
                "'LIBS= -lsqlite3 -lffi -lcrypto1.1 -lssl1.1 -lz' "
                "'CPPFLAGS=-DANDROID "
                '-I/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/include '
                '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/python-installs/myapp/arm64-v8a/include/python3.1 '
                '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/sqlite3/arm64-v8a__ndk_target_21/sqlite3 '
                '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/libffi/arm64-v8a__ndk_target_21/libffi/include '
                '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include '
                '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include/internal '
                '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include/openssl '
                "-I/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/include'",
 'CONFINCLUDEDIR': '/usr/local/include',
 'CONFINCLUDEPY': '/usr/local/include/python3.11',
 'COREPYTHONPATH': '',
 'COVERAGE_INFO': '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/android-build/coverage.info',
 'COVERAGE_LCOV_OPTIONS': '--rc lcov_branch_coverage=1',
 'COVERAGE_REPORT': '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/android-build/lcov-report',
 'COVERAGE_REPORT_OPTIONS': '--rc lcov_branch_coverage=1 --branch-coverage '
                            '--title "CPython 3.11 LCOV report [commit $(shell '
                            ')]"',
 'CPPFLAGS': '-IObjects -IInclude -IPython -I. '
             '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Include '
             '-DANDROID '
             '-I/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/include '
             '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/python-installs/myapp/arm64-v8a/include/python3.1 '
             '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/sqlite3/arm64-v8a__ndk_target_21/sqlite3 '
             '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/libffi/arm64-v8a__ndk_target_21/libffi/include '
             '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include '
             '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include/internal '
             '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include/openssl '
             '-I/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/include '
             '-DANDROID '
             '-I/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/include '
             '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/python-installs/myapp/arm64-v8a/include/python3.1 '
             '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/sqlite3/arm64-v8a__ndk_target_21/sqlite3 '
             '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/libffi/arm64-v8a__ndk_target_21/libffi/include '
             '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include '
             '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include/internal '
             '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include/openssl '
             '-I/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/include',
 'CXX': '/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/bin/clang++ '
        '-target aarch64-linux-android21 -fomit-frame-pointer -march=armv8-a '
        '-fPIC',
 'DECIMAL_CFLAGS': '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/_decimal/libmpdec '
                   '-DCONFIG_64=1 -DANSI=1 -DHAVE_UINT128_T=1',
 'DECIMAL_LDFLAGS': '-lm Modules/_decimal/libmpdec/libmpdec.a',
 'DEEPFREEZE_DEPS': '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Tools/scripts/deepfreeze.py '
                    '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Programs/_freeze_module.py '
                    '\\',
 'DEEPFREEZE_OBJS': 'Python/deepfreeze/deepfreeze.o',
 'DESTDIRS': '/usr/local /usr/local/lib /usr/local/lib/python3.11 '
             '/usr/local/lib/python3.11/lib-dynload',
 'DESTLIB': '/usr/local/lib/python3.11',
 'DESTPATH': '',
 'DESTSHARED': '/usr/local/lib/python3.11/lib-dynload',
 'DFLAGS': '',
 'DIRMODE': 755,
 'DIST': 'README.rst ChangeLog configure configure.ac acconfig.h pyconfig.h.in '
         'Makefile.pre.in Include Lib Misc Ext-dummy',
 'DISTDIRS': 'Include Lib Misc Ext-dummy',
 'DISTFILES': 'README.rst ChangeLog configure configure.ac acconfig.h '
              'pyconfig.h.in Makefile.pre.in',
 'DLINCLDIR': '.',
 'DLLLIBRARY': '',
 'DOUBLE_IS_ARM_MIXED_ENDIAN_IEEE754': 0,
 'DOUBLE_IS_BIG_ENDIAN_IEEE754': 0,
 'DOUBLE_IS_LITTLE_ENDIAN_IEEE754': 1,
 'DTRACE': '',
 'DTRACE_DEPS': '\\',
 'DTRACE_HEADERS': '',
 'DTRACE_OBJS': '',
 'DYNLOADFILE': 'dynload_shlib.o',
 'ENABLE_IPV6': 1,
 'ENSUREPIP': 'no',
 'EXE': '',
 'EXEMODE': 755,
 'EXPAT_CFLAGS': '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/expat',
 'EXPAT_LDFLAGS': '-lm Modules/expat/libexpat.a',
 'EXPORTSFROM': '',
 'EXPORTSYMS': '',
 'EXTRATESTOPTS': '',
 'EXTRA_CFLAGS': '',
 'EXT_SUFFIX': '.cpython-311.so',
 'FILEMODE': 644,
 'FLOAT_WORDS_BIGENDIAN': 0,
 'FREEZE_MODULE': '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/hostpython3/desktop/hostpython3/native-build/python3 '
                  '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Programs/_freeze_module.py',
 'FREEZE_MODULE_BOOTSTRAP': '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/hostpython3/desktop/hostpython3/native-build/python3 '
                            '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Programs/_freeze_module.py',
 'FREEZE_MODULE_BOOTSTRAP_DEPS': '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Programs/_freeze_module.py',
 'FREEZE_MODULE_DEPS': '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Programs/_freeze_module.py',
 'FROZEN_FILES_IN': '\\',
 'FROZEN_FILES_OUT': '\\',
 'GETPGRP_HAVE_ARG': 0,
 'GITBRANCH': '',
 'GITTAG': '',
 'GITVERSION': '',
 'GNULD': 'yes',
 'HAVE_ACCEPT': 1,
 'HAVE_ACCEPT4': 1,
 'HAVE_ACOSH': 1,
 'HAVE_ADDRINFO': 1,
 'HAVE_ALARM': 1,
 'HAVE_ALIGNED_REQUIRED': 1,
 'HAVE_ALLOCA_H': 1,
 'HAVE_ALTZONE': 0,
 'HAVE_ASINH': 1,
 'HAVE_ASM_TYPES_H': 1,
 'HAVE_ATANH': 1,
 'HAVE_BIND': 1,
 'HAVE_BIND_TEXTDOMAIN_CODESET': 0,
 'HAVE_BLUETOOTH_BLUETOOTH_H': 0,
 'HAVE_BLUETOOTH_H': 0,
 'HAVE_BROKEN_MBSTOWCS': 0,
 'HAVE_BROKEN_NICE': 0,
 'HAVE_BROKEN_PIPE_BUF': 0,
 'HAVE_BROKEN_POLL': 0,
 'HAVE_BROKEN_POSIX_SEMAPHORES': 0,
 'HAVE_BROKEN_PTHREAD_SIGMASK': 0,
 'HAVE_BROKEN_SEM_GETVALUE': 1,
 'HAVE_BROKEN_UNSETENV': 0,
 'HAVE_BUILTIN_ATOMIC': 1,
 'HAVE_BZLIB_H': 0,
 'HAVE_CHFLAGS': 0,
 'HAVE_CHMOD': 1,
 'HAVE_CHOWN': 1,
 'HAVE_CHROOT': 1,
 'HAVE_CLOCK': 1,
 'HAVE_CLOCK_GETRES': 1,
 'HAVE_CLOCK_GETTIME': 1,
 'HAVE_CLOCK_NANOSLEEP': 1,
 'HAVE_CLOCK_SETTIME': 1,
 'HAVE_CLOSE_RANGE': 0,
 'HAVE_COMPUTED_GOTOS': 0,
 'HAVE_CONFSTR': 0,
 'HAVE_CONIO_H': 0,
 'HAVE_CONNECT': 1,
 'HAVE_COPY_FILE_RANGE': 0,
 'HAVE_CRYPT_H': 0,
 'HAVE_CRYPT_R': 0,
 'HAVE_CTERMID': 0,
 'HAVE_CTERMID_R': 0,
 'HAVE_CURSES_FILTER': 0,
 'HAVE_CURSES_H': 0,
 'HAVE_CURSES_HAS_KEY': 0,
 'HAVE_CURSES_IMMEDOK': 0,
 'HAVE_CURSES_IS_PAD': 0,
 'HAVE_CURSES_IS_TERM_RESIZED': 0,
 'HAVE_CURSES_RESIZETERM': 0,
 'HAVE_CURSES_RESIZE_TERM': 0,
 'HAVE_CURSES_SYNCOK': 0,
 'HAVE_CURSES_TYPEAHEAD': 0,
 'HAVE_CURSES_USE_ENV': 0,
 'HAVE_CURSES_WCHGAT': 0,
 'HAVE_DB_H': 0,
 'HAVE_DECL_RTLD_DEEPBIND': 0,
 'HAVE_DECL_RTLD_GLOBAL': 1,
 'HAVE_DECL_RTLD_LAZY': 1,
 'HAVE_DECL_RTLD_LOCAL': 1,
 'HAVE_DECL_RTLD_MEMBER': 0,
 'HAVE_DECL_RTLD_NODELETE': 1,
 'HAVE_DECL_RTLD_NOLOAD': 1,
 'HAVE_DECL_RTLD_NOW': 1,
 'HAVE_DECL_TZNAME': 0,
 'HAVE_DEVICE_MACROS': 1,
 'HAVE_DEV_PTC': 0,
 'HAVE_DEV_PTMX': 1,
 'HAVE_DIRECT_H': 0,
 'HAVE_DIRENT_D_TYPE': 1,
 'HAVE_DIRENT_H': 1,
 'HAVE_DIRFD': 1,
 'HAVE_DLFCN_H': 1,
 'HAVE_DLOPEN': 1,
 'HAVE_DUP': 1,
 'HAVE_DUP2': 1,
 'HAVE_DUP3': 1,
 'HAVE_DYLD_SHARED_CACHE_CONTAINS_PATH': 0,
 'HAVE_DYNAMIC_LOADING': 1,
 'HAVE_ENDIAN_H': 1,
 'HAVE_EPOLL': 1,
 'HAVE_EPOLL_CREATE1': 1,
 'HAVE_ERF': 1,
 'HAVE_ERFC': 1,
 'HAVE_ERRNO_H': 1,
 'HAVE_EVENTFD': 0,
 'HAVE_EXECV': 1,
 'HAVE_EXPLICIT_BZERO': 0,
 'HAVE_EXPLICIT_MEMSET': 0,
 'HAVE_EXPM1': 1,
 'HAVE_FACCESSAT': 1,
 'HAVE_FCHDIR': 1,
 'HAVE_FCHMOD': 1,
 'HAVE_FCHMODAT': 1,
 'HAVE_FCHOWN': 1,
 'HAVE_FCHOWNAT': 1,
 'HAVE_FCNTL_H': 1,
 'HAVE_FDATASYNC': 1,
 'HAVE_FDOPENDIR': 1,
 'HAVE_FDWALK': 0,
 'HAVE_FEXECVE': 0,
 'HAVE_FLOCK': 1,
 'HAVE_FORK': 1,
 'HAVE_FORK1': 0,
 'HAVE_FORKPTY': 0,
 'HAVE_FPATHCONF': 1,
 'HAVE_FSEEK64': 0,
 'HAVE_FSEEKO': 1,
 'HAVE_FSTATAT': 1,
 'HAVE_FSTATVFS': 1,
 'HAVE_FSYNC': 1,
 'HAVE_FTELL64': 0,
 'HAVE_FTELLO': 1,
 'HAVE_FTIME': 0,
 'HAVE_FTRUNCATE': 1,
 'HAVE_FUTIMENS': 1,
 'HAVE_FUTIMES': 0,
 'HAVE_FUTIMESAT': 0,
 'HAVE_GAI_STRERROR': 1,
 'HAVE_GCC_ASM_FOR_MC68881': 0,
 'HAVE_GCC_ASM_FOR_X64': 0,
 'HAVE_GCC_ASM_FOR_X87': 0,
 'HAVE_GCC_UINT128_T': 1,
 'HAVE_GDBM_DASH_NDBM_H': 0,
 'HAVE_GDBM_H': 0,
 'HAVE_GDBM_NDBM_H': 0,
 'HAVE_GETADDRINFO': 1,
 'HAVE_GETC_UNLOCKED': 1,
 'HAVE_GETEGID': 1,
 'HAVE_GETENTROPY': 0,
 'HAVE_GETEUID': 1,
 'HAVE_GETGID': 1,
 'HAVE_GETGRGID': 1,
 'HAVE_GETGRGID_R': 0,
 'HAVE_GETGRNAM_R': 0,
 'HAVE_GETGROUPLIST': 1,
 'HAVE_GETGROUPS': 1,
 'HAVE_GETHOSTBYADDR': 1,
 'HAVE_GETHOSTBYNAME': 1,
 'HAVE_GETHOSTBYNAME_R': 1,
 'HAVE_GETHOSTBYNAME_R_3_ARG': 0,
 'HAVE_GETHOSTBYNAME_R_5_ARG': 0,
 'HAVE_GETHOSTBYNAME_R_6_ARG': 1,
 'HAVE_GETHOSTNAME': 1,
 'HAVE_GETITIMER': 1,
 'HAVE_GETLOADAVG': 0,
 'HAVE_GETLOGIN': 1,
 'HAVE_GETNAMEINFO': 1,
 'HAVE_GETPAGESIZE': 1,
 'HAVE_GETPEERNAME': 1,
 'HAVE_GETPGID': 1,
 'HAVE_GETPGRP': 1,
 'HAVE_GETPID': 1,
 'HAVE_GETPPID': 1,
 'HAVE_GETPRIORITY': 1,
 'HAVE_GETPROTOBYNAME': 1,
 'HAVE_GETPWENT': 0,
 'HAVE_GETPWNAM_R': 1,
 'HAVE_GETPWUID': 1,
 'HAVE_GETPWUID_R': 1,
 'HAVE_GETRANDOM': 0,
 'HAVE_GETRANDOM_SYSCALL': 1,
 'HAVE_GETRESGID': 1,
 'HAVE_GETRESUID': 1,
 'HAVE_GETRUSAGE': 1,
 'HAVE_GETSERVBYNAME': 1,
 'HAVE_GETSERVBYPORT': 1,
 'HAVE_GETSID': 1,
 'HAVE_GETSOCKNAME': 1,
 'HAVE_GETSPENT': 0,
 'HAVE_GETSPNAM': 0,
 'HAVE_GETUID': 1,
 'HAVE_GETWD': 0,
 'HAVE_GLIBC_MEMMOVE_BUG': 0,
 'HAVE_GRP_H': 1,
 'HAVE_HSTRERROR': 1,
 'HAVE_HTOLE64': 1,
 'HAVE_IEEEFP_H': 0,
 'HAVE_IF_NAMEINDEX': 0,
 'HAVE_INET_ATON': 1,
 'HAVE_INET_NTOA': 1,
 'HAVE_INET_PTON': 1,
 'HAVE_INITGROUPS': 1,
 'HAVE_INTTYPES_H': 1,
 'HAVE_IO_H': 0,
 'HAVE_IPA_PURE_CONST_BUG': 0,
 'HAVE_KILL': 1,
 'HAVE_KILLPG': 1,
 'HAVE_KQUEUE': 0,
 'HAVE_LANGINFO_H': 1,
 'HAVE_LARGEFILE_SUPPORT': 0,
 'HAVE_LCHFLAGS': 0,
 'HAVE_LCHMOD': 0,
 'HAVE_LCHOWN': 1,
 'HAVE_LIBB2': 1,
 'HAVE_LIBDB': 0,
 'HAVE_LIBDL': 1,
 'HAVE_LIBDLD': 0,
 'HAVE_LIBGDBM_COMPAT': 0,
 'HAVE_LIBIEEE': 0,
 'HAVE_LIBINTL_H': 0,
 'HAVE_LIBNDBM': 0,
 'HAVE_LIBREADLINE': 0,
 'HAVE_LIBRESOLV': 0,
 'HAVE_LIBSENDFILE': 0,
 'HAVE_LIBSQLITE3': 1,
 'HAVE_LIBUTIL_H': 0,
 'HAVE_LINK': 1,
 'HAVE_LINKAT': 1,
 'HAVE_LINUX_AUXVEC_H': 1,
 'HAVE_LINUX_CAN_BCM_H': 1,
 'HAVE_LINUX_CAN_H': 1,
 'HAVE_LINUX_CAN_J1939_H': 1,
 'HAVE_LINUX_CAN_RAW_FD_FRAMES': 1,
 'HAVE_LINUX_CAN_RAW_H': 1,
 'HAVE_LINUX_CAN_RAW_JOIN_FILTERS': 1,
 'HAVE_LINUX_LIMITS_H': 1,
 'HAVE_LINUX_MEMFD_H': 1,
 'HAVE_LINUX_NETLINK_H': 1,
 'HAVE_LINUX_QRTR_H': 1,
 'HAVE_LINUX_RANDOM_H': 1,
 'HAVE_LINUX_SOUNDCARD_H': 1,
 'HAVE_LINUX_TIPC_H': 1,
 'HAVE_LINUX_VM_SOCKETS_H': 1,
 'HAVE_LINUX_WAIT_H': 1,
 'HAVE_LISTEN': 1,
 'HAVE_LOCKF': 0,
 'HAVE_LOG1P': 1,
 'HAVE_LOG2': 1,
 'HAVE_LOGIN_TTY': 0,
 'HAVE_LONG_DOUBLE': 1,
 'HAVE_LSTAT': 1,
 'HAVE_LUTIMES': 0,
 'HAVE_LZMA_H': 0,
 'HAVE_MADVISE': 1,
 'HAVE_MAKEDEV': 1,
 'HAVE_MBRTOWC': 1,
 'HAVE_MEMFD_CREATE': 0,
 'HAVE_MEMORY_H': 1,
 'HAVE_MEMRCHR': 1,
 'HAVE_MKDIRAT': 1,
 'HAVE_MKFIFO': 1,
 'HAVE_MKFIFOAT': 0,
 'HAVE_MKNOD': 1,
 'HAVE_MKNODAT': 1,
 'HAVE_MKTIME': 1,
 'HAVE_MMAP': 1,
 'HAVE_MREMAP': 1,
 'HAVE_NANOSLEEP': 1,
 'HAVE_NCURSES_H': 0,
 'HAVE_NDBM_H': 0,
 'HAVE_NDIR_H': 0,
 'HAVE_NETCAN_CAN_H': 0,
 'HAVE_NETDB_H': 1,
 'HAVE_NETINET_IN_H': 1,
 'HAVE_NETPACKET_PACKET_H': 1,
 'HAVE_NET_IF_H': 1,
 'HAVE_NICE': 1,
 'HAVE_NON_UNICODE_WCHAR_T_REPRESENTATION': 0,
 'HAVE_OPENAT': 1,
 'HAVE_OPENDIR': 1,
 'HAVE_OPENPTY': 0,
 'HAVE_PATHCONF': 1,
 'HAVE_PAUSE': 1,
 'HAVE_PIPE': 1,
 'HAVE_PIPE2': 1,
 'HAVE_PLOCK': 0,
 'HAVE_POLL': 1,
 'HAVE_POLL_H': 1,
 'HAVE_POSIX_FADVISE': 1,
 'HAVE_POSIX_FALLOCATE': 1,
 'HAVE_POSIX_SPAWN': 0,
 'HAVE_POSIX_SPAWNP': 0,
 'HAVE_PREAD': 1,
 'HAVE_PREADV': 0,
 'HAVE_PREADV2': 0,
 'HAVE_PRLIMIT': 1,
 'HAVE_PROCESS_H': 0,
 'HAVE_PROTOTYPES': 1,
 'HAVE_PTHREAD_CONDATTR_SETCLOCK': 1,
 'HAVE_PTHREAD_DESTRUCTOR': 0,
 'HAVE_PTHREAD_GETCPUCLOCKID': 1,
 'HAVE_PTHREAD_H': 1,
 'HAVE_PTHREAD_INIT': 0,
 'HAVE_PTHREAD_KILL': 1,
 'HAVE_PTHREAD_SIGMASK': 1,
 'HAVE_PTHREAD_STUBS': 0,
 'HAVE_PTY_H': 1,
 'HAVE_PWRITE': 1,
 'HAVE_PWRITEV': 0,
 'HAVE_PWRITEV2': 0,
 'HAVE_READLINK': 1,
 'HAVE_READLINKAT': 1,
 'HAVE_READV': 1,
 'HAVE_REALPATH': 1,
 'HAVE_RECVFROM': 1,
 'HAVE_RENAMEAT': 1,
 'HAVE_RL_APPEND_HISTORY': 0,
 'HAVE_RL_CATCH_SIGNAL': 0,
 'HAVE_RL_COMPLETION_APPEND_CHARACTER': 0,
 'HAVE_RL_COMPLETION_DISPLAY_MATCHES_HOOK': 0,
 'HAVE_RL_COMPLETION_MATCHES': 0,
 'HAVE_RL_COMPLETION_SUPPRESS_APPEND': 0,
 'HAVE_RL_PRE_INPUT_HOOK': 0,
 'HAVE_RL_RESIZE_TERMINAL': 0,
 'HAVE_RPC_RPC_H': 0,
 'HAVE_RTPSPAWN': 0,
 'HAVE_SCHED_GET_PRIORITY_MAX': 1,
 'HAVE_SCHED_H': 1,
 'HAVE_SCHED_RR_GET_INTERVAL': 1,
 'HAVE_SCHED_SETAFFINITY': 1,
 'HAVE_SCHED_SETPARAM': 1,
 'HAVE_SCHED_SETSCHEDULER': 1,
 'HAVE_SEM_CLOCKWAIT': 0,
 'HAVE_SEM_GETVALUE': 1,
 'HAVE_SEM_OPEN': 1,
 'HAVE_SEM_TIMEDWAIT': 1,
 'HAVE_SEM_UNLINK': 1,
 'HAVE_SENDFILE': 1,
 'HAVE_SENDTO': 1,
 'HAVE_SETEGID': 1,
 'HAVE_SETEUID': 1,
 'HAVE_SETGID': 1,
 'HAVE_SETGROUPS': 1,
 'HAVE_SETHOSTNAME': 0,
 'HAVE_SETITIMER': 1,
 'HAVE_SETJMP_H': 1,
 'HAVE_SETLOCALE': 1,
 'HAVE_SETPGID': 1,
 'HAVE_SETPGRP': 1,
 'HAVE_SETPRIORITY': 1,
 'HAVE_SETREGID': 1,
 'HAVE_SETRESGID': 1,
 'HAVE_SETRESUID': 1,
 'HAVE_SETREUID': 1,
 'HAVE_SETSID': 1,
 'HAVE_SETSOCKOPT': 1,
 'HAVE_SETUID': 1,
 'HAVE_SETVBUF': 1,
 'HAVE_SHADOW_H': 0,
 'HAVE_SHM_OPEN': 0,
 'HAVE_SHM_UNLINK': 0,
 'HAVE_SHUTDOWN': 1,
 'HAVE_SIGACTION': 1,
 'HAVE_SIGALTSTACK': 1,
 'HAVE_SIGFILLSET': 1,
 'HAVE_SIGINFO_T_SI_BAND': 1,
 'HAVE_SIGINTERRUPT': 1,
 'HAVE_SIGNAL_H': 1,
 'HAVE_SIGPENDING': 1,
 'HAVE_SIGRELSE': 0,
 'HAVE_SIGTIMEDWAIT': 0,
 'HAVE_SIGWAIT': 1,
 'HAVE_SIGWAITINFO': 0,
 'HAVE_SNPRINTF': 1,
 'HAVE_SOCKADDR_ALG': 1,
 'HAVE_SOCKADDR_SA_LEN': 0,
 'HAVE_SOCKADDR_STORAGE': 1,
 'HAVE_SOCKET': 1,
 'HAVE_SOCKETPAIR': 1,
 'HAVE_SPAWN_H': 1,
 'HAVE_SPLICE': 1,
 'HAVE_SSIZE_T': 1,
 'HAVE_STATVFS': 1,
 'HAVE_STAT_TV_NSEC': 1,
 'HAVE_STAT_TV_NSEC2': 0,
 'HAVE_STDARG_PROTOTYPES': 1,
 'HAVE_STDINT_H': 1,
 'HAVE_STDLIB_H': 1,
 'HAVE_STD_ATOMIC': 1,
 'HAVE_STRFTIME': 1,
 'HAVE_STRINGS_H': 1,
 'HAVE_STRING_H': 1,
 'HAVE_STRLCPY': 1,
 'HAVE_STROPTS_H': 0,
 'HAVE_STRSIGNAL': 1,
 'HAVE_STRUCT_PASSWD_PW_GECOS': 1,
 'HAVE_STRUCT_PASSWD_PW_PASSWD': 1,
 'HAVE_STRUCT_STAT_ST_BIRTHTIME': 0,
 'HAVE_STRUCT_STAT_ST_BLKSIZE': 1,
 'HAVE_STRUCT_STAT_ST_BLOCKS': 1,
 'HAVE_STRUCT_STAT_ST_FLAGS': 0,
 'HAVE_STRUCT_STAT_ST_GEN': 0,
 'HAVE_STRUCT_STAT_ST_RDEV': 1,
 'HAVE_STRUCT_TM_TM_ZONE': 1,
 'HAVE_SYMLINK': 1,
 'HAVE_SYMLINKAT': 1,
 'HAVE_SYNC': 1,
 'HAVE_SYSCONF': 1,
 'HAVE_SYSEXITS_H': 1,
 'HAVE_SYSLOG_H': 1,
 'HAVE_SYSTEM': 1,
 'HAVE_SYS_AUDIOIO_H': 0,
 'HAVE_SYS_AUXV_H': 1,
 'HAVE_SYS_BSDTTY_H': 0,
 'HAVE_SYS_DEVPOLL_H': 0,
 'HAVE_SYS_DIR_H': 0,
 'HAVE_SYS_ENDIAN_H': 1,
 'HAVE_SYS_EPOLL_H': 1,
 'HAVE_SYS_EVENTFD_H': 0,
 'HAVE_SYS_EVENT_H': 0,
 'HAVE_SYS_FILE_H': 1,
 'HAVE_SYS_IOCTL_H': 1,
 'HAVE_SYS_KERN_CONTROL_H': 0,
 'HAVE_SYS_LOADAVG_H': 0,
 'HAVE_SYS_LOCK_H': 0,
 'HAVE_SYS_MEMFD_H': 0,
 'HAVE_SYS_MKDEV_H': 0,
 'HAVE_SYS_MMAN_H': 1,
 'HAVE_SYS_MODEM_H': 0,
 'HAVE_SYS_NDIR_H': 0,
 'HAVE_SYS_PARAM_H': 1,
 'HAVE_SYS_POLL_H': 1,
 'HAVE_SYS_RANDOM_H': 1,
 'HAVE_SYS_RESOURCE_H': 1,
 'HAVE_SYS_SELECT_H': 1,
 'HAVE_SYS_SENDFILE_H': 1,
 'HAVE_SYS_SOCKET_H': 1,
 'HAVE_SYS_SOUNDCARD_H': 0,
 'HAVE_SYS_STATVFS_H': 1,
 'HAVE_SYS_STAT_H': 1,
 'HAVE_SYS_SYSCALL_H': 1,
 'HAVE_SYS_SYSMACROS_H': 1,
 'HAVE_SYS_SYS_DOMAIN_H': 0,
 'HAVE_SYS_TERMIO_H': 0,
 'HAVE_SYS_TIMES_H': 1,
 'HAVE_SYS_TIME_H': 1,
 'HAVE_SYS_TYPES_H': 1,
 'HAVE_SYS_UIO_H': 1,
 'HAVE_SYS_UN_H': 1,
 'HAVE_SYS_UTSNAME_H': 1,
 'HAVE_SYS_WAIT_H': 1,
 'HAVE_SYS_XATTR_H': 1,
 'HAVE_TCGETPGRP': 1,
 'HAVE_TCSETPGRP': 1,
 'HAVE_TEMPNAM': 1,
 'HAVE_TERMIOS_H': 1,
 'HAVE_TERM_H': 0,
 'HAVE_TIMEGM': 1,
 'HAVE_TIMES': 1,
 'HAVE_TMPFILE': 1,
 'HAVE_TMPNAM': 1,
 'HAVE_TMPNAM_R': 0,
 'HAVE_TM_ZONE': 1,
 'HAVE_TRUNCATE': 1,
 'HAVE_TTYNAME': 1,
 'HAVE_TZNAME': 0,
 'HAVE_UMASK': 1,
 'HAVE_UNAME': 1,
 'HAVE_UNISTD_H': 1,
 'HAVE_UNLINKAT': 1,
 'HAVE_USABLE_WCHAR_T': 0,
 'HAVE_UTIL_H': 0,
 'HAVE_UTIMENSAT': 1,
 'HAVE_UTIMES': 1,
 'HAVE_UTIME_H': 1,
 'HAVE_UTMP_H': 1,
 'HAVE_UUID_CREATE': 0,
 'HAVE_UUID_ENC_BE': 0,
 'HAVE_UUID_GENERATE_TIME_SAFE': 0,
 'HAVE_UUID_H': 0,
 'HAVE_UUID_UUID_H': 0,
 'HAVE_VFORK': 1,
 'HAVE_WAIT': 1,
 'HAVE_WAIT3': 0,
 'HAVE_WAIT4': 1,
 'HAVE_WAITID': 1,
 'HAVE_WAITPID': 1,
 'HAVE_WCHAR_H': 1,
 'HAVE_WCSCOLL': 1,
 'HAVE_WCSFTIME': 1,
 'HAVE_WCSXFRM': 1,
 'HAVE_WMEMCMP': 1,
 'HAVE_WORKING_TZSET': 0,
 'HAVE_WRITEV': 1,
 'HAVE_ZLIB_COPY': 1,
 'HAVE_ZLIB_H': 0,
 'HAVE__GETPTY': 0,
 'HOSTRUNNER': '',
 'HOST_GNU_TYPE': 'aarch64-unknown-linux-android',
 'INCLDIRSTOMAKE': '/usr/local/include /usr/local/include '
                   '/usr/local/include/python3.11 '
                   '/usr/local/include/python3.11',
 'INCLUDEDIR': '/usr/local/include',
 'INCLUDEPY': '/usr/local/include/python3.11',
 'INSTALL': '/usr/bin/install -c',
 'INSTALL_DATA': '/usr/bin/install -c -m 644',
 'INSTALL_PROGRAM': '/usr/bin/install -c',
 'INSTALL_SCRIPT': '/usr/bin/install -c',
 'INSTALL_SHARED': '/usr/bin/install -c -m 755',
 'INSTSONAME': 'libpython3.11.so.1.0',
 'IO_H': 'Modules/_io/_iomodule.h',
 'IO_OBJS': '\\',
 'LDCXXSHARED': '/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/bin/clang '
                '-target aarch64-linux-android21 -fomit-frame-pointer '
                '-march=armv8-a -fPIC -pthread -shared -Wl,-O1 '
                '-Wl,-Bsymbolic-functions',
 'LDFLAGS': '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/libs_collections/myapp/arm64-v8a '
            '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/sqlite3/arm64-v8a__ndk_target_21/sqlite3/obj/local/arm64-v8a '
            '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/libffi/arm64-v8a__ndk_target_21/libffi/.libs '
            '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1 '
            '-L/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/lib/aarch64-linux-android/21   '
            '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/libs_collections/myapp/arm64-v8a '
            '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/sqlite3/arm64-v8a__ndk_target_21/sqlite3/obj/local/arm64-v8a '
            '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/libffi/arm64-v8a__ndk_target_21/libffi/.libs '
            '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1 '
            '-L/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/lib/aarch64-linux-android/21',
 'LDFLAGS_NODIST': '',
 'LDLIBRARY': 'libpython3.11.so',
 'LDLIBRARYDIR': '',
 'LDSHARED': '/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/bin/clang '
             '-target aarch64-linux-android21 -fomit-frame-pointer '
             '-march=armv8-a -fPIC -pthread -shared -Wl,-O1 '
             '-Wl,-Bsymbolic-functions '
             '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/libs_collections/myapp/arm64-v8a '
             '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/sqlite3/arm64-v8a__ndk_target_21/sqlite3/obj/local/arm64-v8a '
             '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/libffi/arm64-v8a__ndk_target_21/libffi/.libs '
             '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1 '
             '-L/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/lib/aarch64-linux-android/21   '
             '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/libs_collections/myapp/arm64-v8a '
             '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/sqlite3/arm64-v8a__ndk_target_21/sqlite3/obj/local/arm64-v8a '
             '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/libffi/arm64-v8a__ndk_target_21/libffi/.libs '
             '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1 '
             '-L/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/lib/aarch64-linux-android/21',
 'LDVERSION': '3.11',
 'LIBC': '',
 'LIBDEST': '/usr/local/lib/python3.11',
 'LIBDIR': '/usr/local/lib',
 'LIBEXPAT_A': 'Modules/expat/libexpat.a',
 'LIBEXPAT_CFLAGS': '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/expat '
                    '-DNDEBUG -g -fwrapv -O3 -Wall -fPIC -DANDROID -fPIC '
                    '-DANDROID -std=c11 -Werror=implicit-function-declaration '
                    '-fvisibility=hidden  '
                    '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Include/internal '
                    '-IObjects -IInclude -IPython -I. '
                    '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Include '
                    '-DANDROID '
                    '-I/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/include '
                    '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/python-installs/myapp/arm64-v8a/include/python3.1 '
                    '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/sqlite3/arm64-v8a__ndk_target_21/sqlite3 '
                    '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/libffi/arm64-v8a__ndk_target_21/libffi/include '
                    '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include '
                    '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include/internal '
                    '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include/openssl '
                    '-I/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/include '
                    '-DANDROID '
                    '-I/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/include '
                    '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/python-installs/myapp/arm64-v8a/include/python3.1 '
                    '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/sqlite3/arm64-v8a__ndk_target_21/sqlite3 '
                    '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/libffi/arm64-v8a__ndk_target_21/libffi/include '
                    '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include '
                    '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include/internal '
                    '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include/openssl '
                    '-I/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/include',
 'LIBEXPAT_HEADERS': '\\',
 'LIBEXPAT_OBJS': '\\',
 'LIBFFI_INCLUDEDIR': '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/libffi/arm64-v8a__ndk_target_21/libffi/include',
 'LIBM': '-lm',
 'LIBMPDEC_A': 'Modules/_decimal/libmpdec/libmpdec.a',
 'LIBMPDEC_CFLAGS': '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/_decimal/libmpdec '
                    '-DCONFIG_64=1 -DANSI=1 -DHAVE_UINT128_T=1 -DNDEBUG -g '
                    '-fwrapv -O3 -Wall -fPIC -DANDROID -fPIC -DANDROID '
                    '-std=c11 -Werror=implicit-function-declaration '
                    '-fvisibility=hidden  '
                    '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Include/internal '
                    '-IObjects -IInclude -IPython -I. '
                    '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Include '
                    '-DANDROID '
                    '-I/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/include '
                    '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/python-installs/myapp/arm64-v8a/include/python3.1 '
                    '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/sqlite3/arm64-v8a__ndk_target_21/sqlite3 '
                    '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/libffi/arm64-v8a__ndk_target_21/libffi/include '
                    '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include '
                    '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include/internal '
                    '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include/openssl '
                    '-I/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/include '
                    '-DANDROID '
                    '-I/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/include '
                    '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/python-installs/myapp/arm64-v8a/include/python3.1 '
                    '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/sqlite3/arm64-v8a__ndk_target_21/sqlite3 '
                    '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/libffi/arm64-v8a__ndk_target_21/libffi/include '
                    '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include '
                    '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include/internal '
                    '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include/openssl '
                    '-I/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/include',
 'LIBMPDEC_HEADERS': '\\',
 'LIBMPDEC_OBJS': '\\',
 'LIBOBJDIR': 'Python/',
 'LIBOBJS': '',
 'LIBPC': '/usr/local/lib/pkgconfig',
 'LIBPL': '/usr/local/lib/python3.11/config-3.11',
 'LIBPYTHON': '-lpython3.11',
 'LIBRARY': 'libpython3.11.a',
 'LIBRARY_DEPS': 'libpython3.11.a libpython3.11.so libpython3.so',
 'LIBRARY_OBJS': '\\',
 'LIBRARY_OBJS_OMIT_FROZEN': '\\',
 'LIBS': '-ldl  -lsqlite3 -lffi -lcrypto1.1 -lssl1.1 -lz',
 'LIBSUBDIRS': 'asyncio \\',
 'LINKCC': '/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/bin/aarch64-linux-android21-clang',
 'LINKFORSHARED': '-pie -Xlinker -export-dynamic',
 'LINK_PYTHON_DEPS': 'libpython3.11.a libpython3.11.so libpython3.so',
 'LINK_PYTHON_OBJS': '-L. -lpython3.11',
 'LIPO_32BIT_FLAGS': '',
 'LIPO_INTEL64_FLAGS': '',
 'LLVM_PROF_ERR': 'no',
 'LLVM_PROF_FILE': 'LLVM_PROFILE_FILE="code-%p.profclangr"',
 'LLVM_PROF_MERGER': '/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/bin/llvm-profdata '
                     'merge -output=code.profclangd *.profclangr',
 'LN': 'ln',
 'LOCALMODLIBS': '',
 'MACHDEP': 'linux',
 'MACHDEP_OBJS': '',
 'MACHDESTLIB': '/usr/local/lib/python3.11',
 'MACOSX_DEPLOYMENT_TARGET': '',
 'MAINCC': '/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/bin/aarch64-linux-android21-clang',
 'MAJOR_IN_MKDEV': 0,
 'MAJOR_IN_SYSMACROS': 1,
 'MAKESETUP': '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/makesetup',
 'MANDIR': '/usr/local/share/man',
 'MKDIR_P': '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/install-sh '
            '-c -d',
 'MODBUILT_NAMES': 'atexit  faulthandler  posix  _signal  _tracemalloc  '
                   '_codecs  _collections  errno  _io  itertools  _sre  '
                   '_thread  time  _weakref  _abc  _functools  _locale  '
                   '_operator  _stat  _symtable  pwd  xxsubtype',
 'MODDISABLED_NAMES': '',
 'MODLIBS': '',
 'MODOBJS': 'Modules/atexitmodule.o  Modules/faulthandler.o  '
            'Modules/posixmodule.o  Modules/signalmodule.o  '
            'Modules/_tracemalloc.o  Modules/_codecsmodule.o  '
            'Modules/_collectionsmodule.o  Modules/errnomodule.o  '
            'Modules/_io/_iomodule.o Modules/_io/iobase.o Modules/_io/fileio.o '
            'Modules/_io/bytesio.o Modules/_io/bufferedio.o '
            'Modules/_io/textio.o Modules/_io/stringio.o  '
            'Modules/itertoolsmodule.o  Modules/_sre/sre.o  '
            'Modules/_threadmodule.o  Modules/timemodule.o  '
            'Modules/_weakref.o  Modules/_abc.o  Modules/_functoolsmodule.o  '
            'Modules/_localemodule.o  Modules/_operator.o  Modules/_stat.o  '
            'Modules/symtablemodule.o  Modules/pwdmodule.o  '
            'Modules/xxsubtype.o',
 'MODSHARED_NAMES': '',
 'MODULE_ARRAY_STATE': 'yes',
 'MODULE_ATEXIT_LDFLAGS': '',
 'MODULE_AUDIOOP_LDFLAGS': '-lm',
 'MODULE_AUDIOOP_STATE': 'yes',
 'MODULE_BINASCII_CFLAGS': '-DUSE_ZLIB_CRC32',
 'MODULE_BINASCII_LDFLAGS': '-lz',
 'MODULE_BINASCII_STATE': 'yes',
 'MODULE_CMATH_DEPS': '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/_math.h',
 'MODULE_CMATH_LDFLAGS': '-lm',
 'MODULE_CMATH_STATE': 'yes',
 'MODULE_ERRNO_LDFLAGS': '',
 'MODULE_FAULTHANDLER_LDFLAGS': '',
 'MODULE_FCNTL_LDFLAGS': '',
 'MODULE_FCNTL_STATE': 'yes',
 'MODULE_GRP_STATE': 'yes',
 'MODULE_ITERTOOLS_LDFLAGS': '',
 'MODULE_MATH_DEPS': '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/_math.h',
 'MODULE_MATH_LDFLAGS': '-lm',
 'MODULE_MATH_STATE': 'yes',
 'MODULE_MMAP_STATE': 'yes',
 'MODULE_NIS_STATE': 'missing',
 'MODULE_OBJS': '\\',
 'MODULE_OSSAUDIODEV_LDFLAGS': '',
 'MODULE_OSSAUDIODEV_STATE': 'yes',
 'MODULE_POSIX_LDFLAGS': '',
 'MODULE_PWD_LDFLAGS': '',
 'MODULE_PWD_STATE': 'yes',
 'MODULE_PYEXPAT_CFLAGS': '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/expat',
 'MODULE_PYEXPAT_DEPS': '\\ Modules/expat/libexpat.a',
 'MODULE_PYEXPAT_LDFLAGS': '-lm Modules/expat/libexpat.a',
 'MODULE_PYEXPAT_STATE': 'yes',
 'MODULE_RESOURCE_STATE': 'yes',
 'MODULE_SELECT_STATE': 'yes',
 'MODULE_SPWD_STATE': 'missing',
 'MODULE_SYSLOG_STATE': 'yes',
 'MODULE_TERMIOS_STATE': 'yes',
 'MODULE_TIME_LDFLAGS': '',
 'MODULE_TIME_STATE': 'yes',
 'MODULE_UNICODEDATA_DEPS': '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/unicodedata_db.h '
                            '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/unicodename_db.h',
 'MODULE_UNICODEDATA_STATE': 'yes',
 'MODULE_XXLIMITED_35_STATE': 'yes',
 'MODULE_XXLIMITED_STATE': 'yes',
 'MODULE_XXSUBTYPE_LDFLAGS': '',
 'MODULE_ZLIB_CFLAGS': '',
 'MODULE_ZLIB_LDFLAGS': '-lz',
 'MODULE_ZLIB_STATE': 'yes',
 'MODULE__ABC_LDFLAGS': '',
 'MODULE__ASYNCIO_STATE': 'yes',
 'MODULE__BISECT_STATE': 'yes',
 'MODULE__BLAKE2_CFLAGS': '-I/opt/homebrew/Cellar/libb2/0.98.1/include',
 'MODULE__BLAKE2_DEPS': '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/_blake2/impl/blake2-config.h '
                        '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/_blake2/impl/blake2-impl.h '
                        '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/_blake2/impl/blake2.h '
                        '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/_blake2/impl/blake2b-load-sse2.h '
                        '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/_blake2/impl/blake2b-load-sse41.h '
                        '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/_blake2/impl/blake2b-ref.c '
                        '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/_blake2/impl/blake2b-round.h '
                        '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/_blake2/impl/blake2b.c '
                        '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/_blake2/impl/blake2s-load-sse2.h '
                        '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/_blake2/impl/blake2s-load-sse41.h '
                        '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/_blake2/impl/blake2s-load-xop.h '
                        '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/_blake2/impl/blake2s-ref.c '
                        '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/_blake2/impl/blake2s-round.h '
                        '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/_blake2/impl/blake2s.c '
                        '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/_blake2/blake2module.h '
                        '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/hashlib.h',
 'MODULE__BLAKE2_LDFLAGS': '-L/opt/homebrew/Cellar/libb2/0.98.1/lib -lb2',
 'MODULE__BLAKE2_STATE': 'yes',
 'MODULE__BZ2_STATE': 'missing',
 'MODULE__CODECS_CN_STATE': 'yes',
 'MODULE__CODECS_HK_STATE': 'yes',
 'MODULE__CODECS_ISO2022_STATE': 'yes',
 'MODULE__CODECS_JP_STATE': 'yes',
 'MODULE__CODECS_KR_STATE': 'yes',
 'MODULE__CODECS_LDFLAGS': '',
 'MODULE__CODECS_TW_STATE': 'yes',
 'MODULE__COLLECTIONS_LDFLAGS': '',
 'MODULE__CONTEXTVARS_STATE': 'yes',
 'MODULE__CRYPT_STATE': 'missing',
 'MODULE__CSV_STATE': 'yes',
 'MODULE__CTYPES_DEPS': '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/_ctypes/ctypes.h',
 'MODULE__CTYPES_TEST_LDFLAGS': '-lm',
 'MODULE__CTYPES_TEST_STATE': 'yes',
 'MODULE__DATETIME_LDFLAGS': '-lm',
 'MODULE__DATETIME_STATE': 'yes',
 'MODULE__DECIMAL_CFLAGS': '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/_decimal/libmpdec '
                           '-DCONFIG_64=1 -DANSI=1 -DHAVE_UINT128_T=1',
 'MODULE__DECIMAL_DEPS': '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/_decimal/docstrings.h '
                         '\\ Modules/_decimal/libmpdec/libmpdec.a',
 'MODULE__DECIMAL_LDFLAGS': '-lm Modules/_decimal/libmpdec/libmpdec.a',
 'MODULE__DECIMAL_STATE': 'yes',
 'MODULE__ELEMENTTREE_CFLAGS': '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/expat',
 'MODULE__ELEMENTTREE_DEPS': '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/pyexpat.c '
                             '\\ Modules/expat/libexpat.a',
 'MODULE__ELEMENTTREE_STATE': 'yes',
 'MODULE__FUNCTOOLS_LDFLAGS': '',
 'MODULE__GDBM_STATE': 'missing',
 'MODULE__HASHLIB_CFLAGS': '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include',
 'MODULE__HASHLIB_DEPS': '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/hashlib.h',
 'MODULE__HASHLIB_LDFLAGS': '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/lib   '
                            '-lcrypto',
 'MODULE__HASHLIB_STATE': 'yes',
 'MODULE__HEAPQ_STATE': 'yes',
 'MODULE__IO_CFLAGS': '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/_io',
 'MODULE__IO_DEPS': '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/_io/_iomodule.h',
 'MODULE__IO_LDFLAGS': '',
 'MODULE__IO_STATE': 'yes',
 'MODULE__JSON_STATE': 'yes',
 'MODULE__LOCALE_LDFLAGS': '',
 'MODULE__LSPROF_STATE': 'yes',
 'MODULE__LZMA_CFLAGS': '-I/opt/homebrew/Cellar/xz/5.6.2/include',
 'MODULE__LZMA_LDFLAGS': '-L/opt/homebrew/Cellar/xz/5.6.2/lib -llzma',
 'MODULE__LZMA_STATE': 'yes',
 'MODULE__MD5_DEPS': '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/hashlib.h',
 'MODULE__MD5_STATE': 'yes',
 'MODULE__MULTIBYTECODEC_STATE': 'yes',
 'MODULE__MULTIPROCESSING_CFLAGS': '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/_multiprocessing',
 'MODULE__MULTIPROCESSING_STATE': 'yes',
 'MODULE__OPCODE_STATE': 'yes',
 'MODULE__OPERATOR_LDFLAGS': '',
 'MODULE__PICKLE_STATE': 'yes',
 'MODULE__POSIXSHMEM_STATE': 'missing',
 'MODULE__POSIXSUBPROCESS_STATE': 'yes',
 'MODULE__QUEUE_STATE': 'yes',
 'MODULE__RANDOM_STATE': 'yes',
 'MODULE__SCPROXY_STATE': 'n/a',
 'MODULE__SHA1_DEPS': '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/hashlib.h',
 'MODULE__SHA1_STATE': 'yes',
 'MODULE__SHA256_DEPS': '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/hashlib.h',
 'MODULE__SHA256_STATE': 'yes',
 'MODULE__SHA3_DEPS': '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/_sha3/sha3.c '
                      '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/_sha3/sha3.h '
                      '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/hashlib.h',
 'MODULE__SHA3_STATE': 'yes',
 'MODULE__SHA512_DEPS': '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/hashlib.h',
 'MODULE__SHA512_STATE': 'yes',
 'MODULE__SIGNAL_LDFLAGS': '',
 'MODULE__SOCKET_DEPS': '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/socketmodule.h '
                        '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/addrinfo.h '
                        '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/getaddrinfo.c '
                        '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/getnameinfo.c',
 'MODULE__SOCKET_STATE': 'yes',
 'MODULE__SQLITE3_CFLAGS': '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/_sqlite',
 'MODULE__SQLITE3_DEPS': '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/_sqlite/connection.h '
                         '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/_sqlite/cursor.h '
                         '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/_sqlite/microprotocols.h '
                         '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/_sqlite/module.h '
                         '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/_sqlite/prepare_protocol.h '
                         '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/_sqlite/row.h '
                         '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/_sqlite/util.h',
 'MODULE__SQLITE3_LDFLAGS': '-lsqlite3',
 'MODULE__SQLITE3_STATE': 'yes',
 'MODULE__SRE_LDFLAGS': '',
 'MODULE__SSL_CFLAGS': '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include',
 'MODULE__SSL_DEPS': '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/_ssl.h '
                     '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/_ssl/cert.c '
                     '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/_ssl/debughelpers.c '
                     '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/_ssl/misc.c '
                     '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/_ssl_data.h '
                     '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/_ssl_data_111.h '
                     '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/_ssl_data_300.h '
                     '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/socketmodule.h',
 'MODULE__SSL_LDFLAGS': '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/lib  '
                        '-lssl -lcrypto',
 'MODULE__SSL_STATE': 'yes',
 'MODULE__STATISTICS_LDFLAGS': '-lm',
 'MODULE__STATISTICS_STATE': 'yes',
 'MODULE__STAT_LDFLAGS': '',
 'MODULE__STRUCT_STATE': 'yes',
 'MODULE__SYMTABLE_LDFLAGS': '',
 'MODULE__TESTBUFFER_STATE': 'yes',
 'MODULE__TESTCAPI_DEPS': '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Modules/testcapi_long.h',
 'MODULE__TESTCAPI_STATE': 'yes',
 'MODULE__TESTCLINIC_STATE': 'yes',
 'MODULE__TESTIMPORTMULTIPLE_STATE': 'yes',
 'MODULE__TESTINTERNALCAPI_STATE': 'yes',
 'MODULE__TESTMULTIPHASE_STATE': 'yes',
 'MODULE__THREAD_LDFLAGS': '',
 'MODULE__TKINTER_STATE': 'missing',
 'MODULE__TRACEMALLOC_LDFLAGS': '',
 'MODULE__TYPING_STATE': 'yes',
 'MODULE__UUID_STATE': 'missing',
 'MODULE__WEAKREF_LDFLAGS': '',
 'MODULE__XXSUBINTERPRETERS_STATE': 'yes',
 'MODULE__XXTESTFUZZ_STATE': 'yes',
 'MODULE__ZONEINFO_STATE': 'yes',
 'MULTIARCH': 'aarch64-linux-android',
 'MULTIARCH_CPPFLAGS': '-DMULTIARCH=\\"aarch64-linux-android\\"',
 'MVWDELCH_IS_EXPRESSION': 0,
 'NO_AS_NEEDED': '-Wl,--no-as-needed',
 'OBJECT_OBJS': '\\',
 'OPENSSL_INCLUDES': '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include',
 'OPENSSL_LDFLAGS': '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/lib',
 'OPENSSL_LIBS': '-lssl -lcrypto',
 'OPENSSL_RPATH': '',
 'OPT': '-DNDEBUG -g -fwrapv -O3 -Wall',
 'OTHER_LIBTOOL_OPT': '',
 'PACKAGE_BUGREPORT': 0,
 'PACKAGE_NAME': 0,
 'PACKAGE_STRING': 0,
 'PACKAGE_TARNAME': 0,
 'PACKAGE_URL': 0,
 'PACKAGE_VERSION': 0,
 'PARSER_HEADERS': '\\',
 'PARSER_OBJS': '\\ \\ Parser/myreadline.o Parser/tokenizer.o',
 'PEGEN_HEADERS': '\\',
 'PEGEN_OBJS': '\\',
 'PGO_PROF_GEN_FLAG': '-fprofile-instr-generate',
 'PGO_PROF_USE_FLAG': '-fprofile-instr-use=code.profclangd',
 'PLATLIBDIR': 'lib',
 'POBJS': '\\',
 'POSIX_SEMAPHORES_NOT_ENABLED': 0,
 'PROFILE_TASK': '-m test --pgo --timeout=1200',
 'PTHREAD_KEY_T_IS_COMPATIBLE_WITH_INT': 1,
 'PTHREAD_SYSTEM_SCHED_SUPPORTED': 0,
 'PURIFY': '',
 'PY3LIBRARY': 'libpython3.so',
 'PYLONG_BITS_IN_DIGIT': 0,
 'PYTHON': 'python',
 'PYTHONFRAMEWORK': '',
 'PYTHONFRAMEWORKDIR': 'no-framework',
 'PYTHONFRAMEWORKINSTALLDIR': '',
 'PYTHONFRAMEWORKPREFIX': '',
 'PYTHONPATH': '',
 'PYTHON_FOR_BUILD': '_PYTHON_PROJECT_BASE=/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/android-build '
                     '_PYTHON_HOST_PLATFORM=$(_PYTHON_HOST_PLATFORM) '
                     'PYTHONPATH=$(shell test -f pybuilddir.txt && echo '
                     '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/android-build/`cat '
                     'pybuilddir.txt`:)/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Lib '
                     '_PYTHON_SYSCONFIGDATA_NAME=_sysconfigdata__linux_aarch64-linux-android '
                     '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/hostpython3/desktop/hostpython3/native-build/python3',
 'PYTHON_FOR_BUILD_DEPS': '',
 'PYTHON_FOR_FREEZE': '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/hostpython3/desktop/hostpython3/native-build/python3',
 'PYTHON_FOR_REGEN': '',
 'PYTHON_HEADERS': '\\',
 'PYTHON_OBJS': '\\',
 'PY_BUILTIN_HASHLIB_HASHES': '"md5,sha1,sha256,sha512,sha3,blake2"',
 'PY_BUILTIN_MODULE_CFLAGS': '-DNDEBUG -g -fwrapv -O3 -Wall -fPIC -DANDROID '
                             '-fPIC -DANDROID -std=c11 '
                             '-Werror=implicit-function-declaration '
                             '-fvisibility=hidden  '
                             '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Include/internal '
                             '-IObjects -IInclude -IPython -I. '
                             '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Include '
                             '-DANDROID '
                             '-I/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/include '
                             '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/python-installs/myapp/arm64-v8a/include/python3.1 '
                             '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/sqlite3/arm64-v8a__ndk_target_21/sqlite3 '
                             '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/libffi/arm64-v8a__ndk_target_21/libffi/include '
                             '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include '
                             '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include/internal '
                             '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include/openssl '
                             '-I/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/include '
                             '-DANDROID '
                             '-I/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/include '
                             '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/python-installs/myapp/arm64-v8a/include/python3.1 '
                             '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/sqlite3/arm64-v8a__ndk_target_21/sqlite3 '
                             '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/libffi/arm64-v8a__ndk_target_21/libffi/include '
                             '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include '
                             '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include/internal '
                             '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include/openssl '
                             '-I/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/include '
                             '-DPy_BUILD_CORE_BUILTIN',
 'PY_CFLAGS': '-DNDEBUG -g -fwrapv -O3 -Wall -fPIC -DANDROID -fPIC -DANDROID',
 'PY_CFLAGS_NODIST': '-std=c11 -Werror=implicit-function-declaration '
                     '-fvisibility=hidden  '
                     '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Include/internal',
 'PY_COERCE_C_LOCALE': 1,
 'PY_CORE_CFLAGS': '-DNDEBUG -g -fwrapv -O3 -Wall -fPIC -DANDROID -fPIC '
                   '-DANDROID -std=c11 -Werror=implicit-function-declaration '
                   '-fvisibility=hidden  '
                   '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Include/internal '
                   '-IObjects -IInclude -IPython -I. '
                   '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Include '
                   '-DANDROID '
                   '-I/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/include '
                   '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/python-installs/myapp/arm64-v8a/include/python3.1 '
                   '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/sqlite3/arm64-v8a__ndk_target_21/sqlite3 '
                   '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/libffi/arm64-v8a__ndk_target_21/libffi/include '
                   '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include '
                   '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include/internal '
                   '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include/openssl '
                   '-I/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/include '
                   '-DANDROID '
                   '-I/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/include '
                   '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/python-installs/myapp/arm64-v8a/include/python3.1 '
                   '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/sqlite3/arm64-v8a__ndk_target_21/sqlite3 '
                   '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/libffi/arm64-v8a__ndk_target_21/libffi/include '
                   '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include '
                   '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include/internal '
                   '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include/openssl '
                   '-I/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/include '
                   '-DPy_BUILD_CORE',
 'PY_CORE_LDFLAGS': '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/libs_collections/myapp/arm64-v8a '
                    '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/sqlite3/arm64-v8a__ndk_target_21/sqlite3/obj/local/arm64-v8a '
                    '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/libffi/arm64-v8a__ndk_target_21/libffi/.libs '
                    '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1 '
                    '-L/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/lib/aarch64-linux-android/21   '
                    '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/libs_collections/myapp/arm64-v8a '
                    '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/sqlite3/arm64-v8a__ndk_target_21/sqlite3/obj/local/arm64-v8a '
                    '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/libffi/arm64-v8a__ndk_target_21/libffi/.libs '
                    '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1 '
                    '-L/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/lib/aarch64-linux-android/21',
 'PY_CPPFLAGS': '-IObjects -IInclude -IPython -I. '
                '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Include '
                '-DANDROID '
                '-I/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/include '
                '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/python-installs/myapp/arm64-v8a/include/python3.1 '
                '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/sqlite3/arm64-v8a__ndk_target_21/sqlite3 '
                '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/libffi/arm64-v8a__ndk_target_21/libffi/include '
                '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include '
                '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include/internal '
                '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include/openssl '
                '-I/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/include '
                '-DANDROID '
                '-I/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/include '
                '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/python-installs/myapp/arm64-v8a/include/python3.1 '
                '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/sqlite3/arm64-v8a__ndk_target_21/sqlite3 '
                '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/libffi/arm64-v8a__ndk_target_21/libffi/include '
                '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include '
                '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include/internal '
                '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include/openssl '
                '-I/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/include',
 'PY_ENABLE_SHARED': 1,
 'PY_FORMAT_SIZE_T': '"z"',
 'PY_LDFLAGS': '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/libs_collections/myapp/arm64-v8a '
               '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/sqlite3/arm64-v8a__ndk_target_21/sqlite3/obj/local/arm64-v8a '
               '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/libffi/arm64-v8a__ndk_target_21/libffi/.libs '
               '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1 '
               '-L/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/lib/aarch64-linux-android/21   '
               '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/libs_collections/myapp/arm64-v8a '
               '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/sqlite3/arm64-v8a__ndk_target_21/sqlite3/obj/local/arm64-v8a '
               '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/libffi/arm64-v8a__ndk_target_21/libffi/.libs '
               '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1 '
               '-L/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/lib/aarch64-linux-android/21',
 'PY_LDFLAGS_NODIST': '',
 'PY_LDFLAGS_NOLTO': '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/libs_collections/myapp/arm64-v8a '
                     '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/sqlite3/arm64-v8a__ndk_target_21/sqlite3/obj/local/arm64-v8a '
                     '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/libffi/arm64-v8a__ndk_target_21/libffi/.libs '
                     '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1 '
                     '-L/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/lib/aarch64-linux-android/21   '
                     '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/libs_collections/myapp/arm64-v8a '
                     '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/sqlite3/arm64-v8a__ndk_target_21/sqlite3/obj/local/arm64-v8a '
                     '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/libffi/arm64-v8a__ndk_target_21/libffi/.libs '
                     '-L/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1 '
                     '-L/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/lib/aarch64-linux-android/21',
 'PY_SQLITE_ENABLE_LOAD_EXTENSION': 1,
 'PY_SQLITE_HAVE_SERIALIZE': 0,
 'PY_SSL_DEFAULT_CIPHERS': 1,
 'PY_SSL_DEFAULT_CIPHER_STRING': 0,
 'PY_STDMODULE_CFLAGS': '-DNDEBUG -g -fwrapv -O3 -Wall -fPIC -DANDROID -fPIC '
                        '-DANDROID -std=c11 '
                        '-Werror=implicit-function-declaration '
                        '-fvisibility=hidden  '
                        '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Include/internal '
                        '-IObjects -IInclude -IPython -I. '
                        '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Include '
                        '-DANDROID '
                        '-I/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/include '
                        '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/python-installs/myapp/arm64-v8a/include/python3.1 '
                        '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/sqlite3/arm64-v8a__ndk_target_21/sqlite3 '
                        '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/libffi/arm64-v8a__ndk_target_21/libffi/include '
                        '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include '
                        '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include/internal '
                        '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include/openssl '
                        '-I/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/include '
                        '-DANDROID '
                        '-I/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/include '
                        '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/python-installs/myapp/arm64-v8a/include/python3.1 '
                        '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/sqlite3/arm64-v8a__ndk_target_21/sqlite3 '
                        '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/libffi/arm64-v8a__ndk_target_21/libffi/include '
                        '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include '
                        '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include/internal '
                        '-I/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/openssl/arm64-v8a__ndk_target_21/openssl1.1/include/openssl '
                        '-I/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/include',
 'PY_SUPPORT_TIER': 0,
 'Py_DEBUG': 0,
 'Py_ENABLE_SHARED': 1,
 'Py_HASH_ALGORITHM': 0,
 'Py_STATS': 0,
 'Py_TRACE_REFS': 0,
 'QUICKTESTOPTS': '-x test_subprocess test_io test_lib2to3 \\',
 'READELF': '/Users/walidoutaleb/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/bin/llvm-readelf',
 'RESSRCDIR': 'Mac/Resources/framework',
 'RETSIGTYPE': 'void',
 'RUNSHARED': '',
 'SCRIPTDIR': '/usr/local/lib',
 'SETPGRP_HAVE_ARG': 0,
 'SHELL': '/bin/sh',
 'SHLIBS': '-ldl  -lsqlite3 -lffi -lcrypto1.1 -lssl1.1 -lz',
 'SHLIB_SUFFIX': '.so',
 'SIGNED_RIGHT_SHIFT_ZERO_FILLS': 0,
 'SITEPATH': '',
 'SIZEOF_DOUBLE': 8,
 'SIZEOF_FLOAT': 4,
 'SIZEOF_FPOS_T': 8,
 'SIZEOF_INT': 4,
 'SIZEOF_LONG': 8,
 'SIZEOF_LONG_DOUBLE': 16,
 'SIZEOF_LONG_LONG': 8,
 'SIZEOF_OFF_T': 8,
 'SIZEOF_PID_T': 4,
 'SIZEOF_PTHREAD_KEY_T': 4,
 'SIZEOF_PTHREAD_T': 8,
 'SIZEOF_SHORT': 2,
 'SIZEOF_SIZE_T': 8,
 'SIZEOF_TIME_T': 8,
 'SIZEOF_UINTPTR_T': 8,
 'SIZEOF_VOID_P': 8,
 'SIZEOF_WCHAR_T': 4,
 'SIZEOF__BOOL': 1,
 'SOABI': 'cpython-311',
 'SRCDIRS': 'Modules   Modules/_blake2   Modules/_ctypes   Modules/_decimal   '
            'Modules/_decimal/libmpdec   Modules/_io   '
            'Modules/_multiprocessing   Modules/_sha3   Modules/_sqlite   '
            'Modules/_sre   Modules/_xxtestfuzz   Modules/cjkcodecs   '
            'Modules/expat   Objects   Parser   Programs   Python   '
            'Python/frozen_modules   Python/deepfreeze',
 'SRC_GDB_HOOKS': '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Tools/gdb/libpython.py',
 'STATIC_LIBPYTHON': 1,
 'STDC_HEADERS': 1,
 'STRICT_SYSV_CURSES': "/* Don't use ncurses extensions */",
 'STRIPFLAG': '-s',
 'SUBDIRS': '',
 'SUBDIRSTOO': 'Include Lib Misc',
 'SYSLIBS': '-lm',
 'SYS_SELECT_WITH_SYS_TIME': 1,
 'TESTOPTS': '',
 'TESTPATH': '',
 'TESTPYTHON': '_PYTHON_PROJECT_BASE=/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/android-build '
               '_PYTHON_HOST_PLATFORM=$(_PYTHON_HOST_PLATFORM) '
               'PYTHONPATH=$(shell test -f pybuilddir.txt && echo '
               '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/android-build/`cat '
               'pybuilddir.txt`:)/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Lib '
               '_PYTHON_SYSCONFIGDATA_NAME=_sysconfigdata__linux_aarch64-linux-android '
               '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/hostpython3/desktop/hostpython3/native-build/python3',
 'TESTPYTHONOPTS': '',
 'TESTRUNNER': '_PYTHON_PROJECT_BASE=/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/android-build '
               '_PYTHON_HOST_PLATFORM=$(_PYTHON_HOST_PLATFORM) '
               'PYTHONPATH=$(shell test -f pybuilddir.txt && echo '
               '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/android-build/`cat '
               'pybuilddir.txt`:)/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Lib '
               '_PYTHON_SYSCONFIGDATA_NAME=_sysconfigdata__linux_aarch64-linux-android '
               '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/hostpython3/desktop/hostpython3/native-build/python3 '
               '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Tools/scripts/run_tests.py',
 'TESTSUBDIRS': 'ctypes/test \\',
 'TESTTIMEOUT': 1200,
 'TEST_MODULES': 'yes',
 'THREAD_STACK_SIZE': 0,
 'TIMEMODULE_LIB': 0,
 'TIME_WITH_SYS_TIME': 1,
 'TM_IN_SYS_TIME': 0,
 'TZPATH': '/usr/share/zoneinfo:/usr/lib/zoneinfo:/usr/share/lib/zoneinfo:/etc/zoneinfo',
 'UNICODE_DEPS': '\\',
 'UNIVERSALSDK': '',
 'UPDATE_FILE': '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/Tools/scripts/update_file.py',
 'USE_COMPUTED_GOTOS': 0,
 'VERSION': '3.11',
 'VPATH': '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3',
 'WASM_ASSETS_DIR': './usr/local',
 'WASM_STDLIB': './usr/local/lib/python3.11/os.py',
 'WHEEL_PKG_DIR': '',
 'WINDOW_HAS_FLAGS': 0,
 'WITH_DECIMAL_CONTEXTVAR': 1,
 'WITH_DOC_STRINGS': 1,
 'WITH_DTRACE': 0,
 'WITH_DYLD': 0,
 'WITH_EDITLINE': 0,
 'WITH_FREELISTS': 1,
 'WITH_LIBINTL': 0,
 'WITH_NEXT_FRAMEWORK': 0,
 'WITH_PYMALLOC': 1,
 'WITH_VALGRIND': 0,
 'X87_DOUBLE_ROUNDING': 0,
 'XMLLIBSUBDIRS': 'xml xml/dom xml/etree xml/parsers xml/sax',
 'abs_builddir': '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/android-build',
 'abs_srcdir': '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3',
 'datarootdir': '/usr/local/share',
 'exec_prefix': '/usr/local',
 'prefix': '/usr/local',
 'srcdir': '/Users/walidoutaleb/workspace/github.com/eikonoklastes/AirShare/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3'}
