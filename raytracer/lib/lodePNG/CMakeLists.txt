file(GLOB_RECURSE SRCS ./*.cpp)
file(GLOB_RECURSE HDRS ./*.h)

if(UNIX)
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fPIC -Wall -pedantic -ansi")
endif()

add_library(lodePNG STATIC ${HDRS} ${SRCS})
target_include_directories(lodePNG PUBLIC SYSTEM .)
