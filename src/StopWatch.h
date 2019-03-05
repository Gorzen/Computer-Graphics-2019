//=============================================================================
//
//   Exercise code for the lecture
//   "Introduction to Computer Graphics"
//   by Prof. Dr. Mario Botsch, Bielefeld University
//
//   Copyright (C) Computer Graphics Group, Bielefeld University.
//
//=============================================================================

#ifndef STOPWATCH_H
#define STOPWATCH_H


//== INCLUDES =================================================================

#ifdef _WIN32
#  include <windows.h>
#else // Unix
#  include <sys/time.h>
#endif

#include <iostream>


//== CLASS DEFINITION =========================================================


/// \class StopWatch StopWatch.h
/// This class implements a simple stop watch, that you can start() and stop()
/// and that returns the elapsed() time in milliseconds.
class StopWatch
{
public:
    
    /// Constructor
    StopWatch()
    {
#ifdef _WIN32 // Windows
        QueryPerformanceFrequency(&freq_);
#endif
    }
    
    
    /// Start time measurement
    void start()
    {
#ifdef _WIN32 // Windows
        QueryPerformanceCounter(&starttime_);
#else // Linux
        starttime_ = current_time();
#endif
    }
    
    
    /// Stop time measurement, return elapsed time in ms
    double stop()
    {
#ifdef _WIN32 // Windows
        QueryPerformanceCounter(&endtime_);
#else // Unix
        endtime_ = current_time();
#endif
        return elapsed();
    }
    
    
    /// Return elapsed time in ms (watch has to be stopped).
    double elapsed() const
    {
#ifdef _WIN32 // Windows
        return ((double)(endtime_.QuadPart - starttime_.QuadPart)
                / (double)freq_.QuadPart * 1000.0f);
#else // Unix
        return ((endtime_.tv_sec  - starttime_.tv_sec )*1000.0 +
                (endtime_.tv_usec - starttime_.tv_usec)*0.001);
#endif
    }
    
    
private:
    
#ifdef _WIN32 // Windows
    
    LARGE_INTEGER starttime_, endtime_;
    LARGE_INTEGER freq_;
    
#else // Unix
    
    timeval current_time() const
    {
        struct timeval tv;
        gettimeofday(&tv, 0);
        return tv;
    }
    
    timeval starttime_, endtime_;
    
#endif
};


//-----------------------------------------------------------------------------


/// output a timer to a stream
inline std::ostream&
operator<<(std::ostream& _os, const StopWatch& _timer)
{
    _os << _timer.elapsed() << " ms";
    return _os;
}


/// @}


//=============================================================================
#endif // STOPWATCH_H defined
//=============================================================================
