# Install script for directory: C:/Users/lucas/Google Drive/Semestre 6/Introduction to Computer Graphics/Git/assignment_0

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "C:/Program Files (x86)/RayTracing")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Debug")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xexamplesx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/DESTINATION" TYPE PROGRAM FILES
    "C:/Users/lucas/Google Drive/Semestre 6/Introduction to Computer Graphics/Git/assignment_0/TBB_ROOT-NOTFOUND/bin/ia32/vc12/tbb.dll"
    "C:/Users/lucas/Google Drive/Semestre 6/Introduction to Computer Graphics/Git/assignment_0/TBB_ROOT-NOTFOUND/bin/ia32/vc12/tbbmalloc.dll"
    "C:/Users/lucas/Google Drive/Semestre 6/Introduction to Computer Graphics/Git/assignment_0/RUNTIME"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xlibx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/DESTINATION" TYPE PROGRAM FILES
    "C:/Users/lucas/Google Drive/Semestre 6/Introduction to Computer Graphics/Git/assignment_0/TBB_ROOT-NOTFOUND/bin/ia32/vc12/tbb.dll"
    "C:/Users/lucas/Google Drive/Semestre 6/Introduction to Computer Graphics/Git/assignment_0/TBB_ROOT-NOTFOUND/bin/ia32/vc12/tbbmalloc.dll"
    "C:/Users/lucas/Google Drive/Semestre 6/Introduction to Computer Graphics/Git/assignment_0/RUNTIME"
    )
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("C:/Users/lucas/Google Drive/Semestre 6/Introduction to Computer Graphics/Git/assignment_0/cmake-build-debug/lib/lodePNG/cmake_install.cmake")
  include("C:/Users/lucas/Google Drive/Semestre 6/Introduction to Computer Graphics/Git/assignment_0/cmake-build-debug/src/cmake_install.cmake")

endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "C:/Users/lucas/Google Drive/Semestre 6/Introduction to Computer Graphics/Git/assignment_0/cmake-build-debug/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
