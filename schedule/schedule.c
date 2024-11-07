#include <stdio.h>
#include <windows.h>
#include <time.h>

void click_mouse(void) {
    mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0);
    mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0);
}

void get_current_time(u_int *hour, u_int *minute, u_int *second) {
    time_t seconds = time(NULL);
    struct tm time_struct = *localtime(&seconds);
    *hour = time_struct.tm_hour;
    *minute = time_struct.tm_min;
    *second = time_struct.tm_sec;
}

void wait(u_int hour, u_int minute, u_int second) {

    u_int curr_h, curr_m, curr_s;
    while (1){
        get_current_time(&curr_h, &curr_m, &curr_s);
        if ( curr_h == hour && curr_m == minute && curr_s == second ){
            click_mouse();
            break;
        }
    }
}

int main(int argc, char** argv) {

    if (argc != 4){
        fprintf(stderr, "Wrong parameter-count!\n");
        return EXIT_FAILURE;
    }
    u_int hour, minute, second;

    hour = strtoul(argv[1], NULL, 10);
    minute = strtoul(argv[2], NULL, 10);
    second = strtoul(argv[3], NULL, 10);

    wait(hour, minute, second);
    return EXIT_SUCCESS;

}
