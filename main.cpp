#include <windows.h>
#include <sstream>
#include <string>
#include <chrono>
#include <fstream>
#include <algorithm>
#include <vector>
#include "array_data.h"

LRESULT CALLBACK WndProc(HWND hwnd, UINT msg, WPARAM wParam, LPARAM lParam);
void mergeArrays(int ar1[], int n1, int ar2[], int n2, int ar3[]);
void mergeRecursive(int ar1[], int n1, int ar2[], int n2, int ar3[]);

// Global variables for UI controls
HWND hEdit1, hEdit2, hResultIterative, hResultRecursive;

void writeLog(const std::string& logPath, const std::vector<double>& times) {
    std::ofstream logFile(logPath, std::ios::app);
    if (logFile.is_open()) {
        for (size_t i = 0; i < times.size(); ++i) {
            logFile << times[i] << "\n";
        }
        logFile.close();
        OutputDebugString("Log written successfully.\n");
    } else {
        MessageBox(NULL, ("Failed to open " + logPath + " for writing.").c_str(), "Error", MB_ICONERROR | MB_OK);
    }
}

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow) {
    WNDCLASS wc = {};
    wc.lpfnWndProc = WndProc;
    wc.hInstance = hInstance;
    wc.lpszClassName = "MergeArrayWindow";

    RegisterClass(&wc);

    HWND hwnd = CreateWindowEx(
        0, "MergeArrayWindow", "Merge Sorted Arrays",
        WS_OVERLAPPEDWINDOW, CW_USEDEFAULT, CW_USEDEFAULT, 700, 750,
        NULL, NULL, hInstance, NULL);

    if (!hwnd) return 0;

    ShowWindow(hwnd, nCmdShow);

    MSG msg = {};
    while (GetMessage(&msg, NULL, 0, 0)) {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    return 0;
}

LRESULT CALLBACK WndProc(HWND hwnd, UINT msg, WPARAM wParam, LPARAM lParam) {
    switch (msg) {
        case WM_CREATE: {
            CreateWindow("STATIC", "Merge Sorted Arrays Program", WS_VISIBLE | WS_CHILD | SS_CENTER,
                         20, 10, 640, 30, hwnd, NULL, NULL, NULL);

            CreateWindow("STATIC", "Array 1 (space-separated):", WS_VISIBLE | WS_CHILD,
                         20, 50, 200, 20, hwnd, NULL, NULL, NULL);
            hEdit1 = CreateWindow("EDIT", "", WS_VISIBLE | WS_CHILD | WS_BORDER | ES_MULTILINE,
                                  20, 70, 640, 25, hwnd, NULL, NULL, NULL);

            CreateWindow("STATIC", "Array 2 (space-separated):", WS_VISIBLE | WS_CHILD,
                         20, 110, 200, 20, hwnd, NULL, NULL, NULL);
            hEdit2 = CreateWindow("EDIT", "", WS_VISIBLE | WS_CHILD | WS_BORDER | ES_MULTILINE,
                                  20, 130, 640, 25, hwnd, NULL, NULL, NULL);

            CreateWindow("BUTTON", "Merge and Sort", WS_VISIBLE | WS_CHILD | BS_DEFPUSHBUTTON,
                         20, 170, 300, 30, hwnd, (HMENU)1, NULL, NULL);

            CreateWindow("BUTTON", "Load Predefined Arrays", WS_VISIBLE | WS_CHILD,
                         360, 170, 300, 30, hwnd, (HMENU)2, NULL, NULL);

            CreateWindow("STATIC", "Iterative Result:", WS_VISIBLE | WS_CHILD,
                         20, 220, 200, 20, hwnd, NULL, NULL, NULL);
            hResultIterative = CreateWindow("EDIT", "", WS_VISIBLE | WS_CHILD | WS_BORDER | ES_READONLY | ES_MULTILINE,
                                           20, 240, 640, 50, hwnd, NULL, NULL, NULL);

            CreateWindow("STATIC", "Recursive Result:", WS_VISIBLE | WS_CHILD,
                         20, 340, 200, 20, hwnd, NULL, NULL, NULL);
            hResultRecursive = CreateWindow("EDIT", "", WS_VISIBLE | WS_CHILD | WS_BORDER | ES_READONLY | ES_MULTILINE,
                                           20, 360, 640, 50, hwnd, NULL, NULL, NULL);

            break;
        }

        case WM_COMMAND: {
            if (LOWORD(wParam) == 1) {
                char buffer1[8192], buffer2[8192];
                GetWindowText(hEdit1, buffer1, 8192);
                GetWindowText(hEdit2, buffer2, 8192);

                int ar1[1000], ar2[1000], ar3[2000];
                int n1 = 0, n2 = 0;

                char* token = strtok(buffer1, " ");
                while (token != NULL) {
                    ar1[n1++] = atoi(token);
                    token = strtok(NULL, " ");
                }

                token = strtok(buffer2, " ");
                while (token != NULL) {
                    ar2[n2++] = atoi(token);
                    token = strtok(NULL, " ");
                }

                std::vector<double> iterativeTimes;
                std::vector<double> recursiveTimes;

                for (int i = 0; i < n1 + n2; ++i) {
                    auto startIterative = std::chrono::high_resolution_clock::now();
                    mergeArrays(ar1, n1, ar2, n2, ar3);
                    auto endIterative = std::chrono::high_resolution_clock::now();
                    std::chrono::duration<double, std::milli> elapsedIterative = endIterative - startIterative;
                    iterativeTimes.push_back(elapsedIterative.count());
                }
                writeLog("iterative_log.txt", iterativeTimes);

                std::sort(ar3, ar3 + n1 + n2);
                std::stringstream resultIterative;
                for (int i = 0; i < n1 + n2; i++) {
                    resultIterative << ar3[i] << " ";
                }
                SetWindowText(hResultIterative, resultIterative.str().c_str());

                for (int i = 0; i < n1 + n2; ++i) {
                    auto startRecursive = std::chrono::high_resolution_clock::now();
                    mergeRecursive(ar1, n1, ar2, n2, ar3);
                    auto endRecursive = std::chrono::high_resolution_clock::now();
                    std::chrono::duration<double, std::milli> elapsedRecursive = endRecursive - startRecursive;
                    recursiveTimes.push_back(elapsedRecursive.count());
                }
                writeLog("recursive_log.txt", recursiveTimes);

                std::sort(ar3, ar3 + n1 + n2);
                std::stringstream resultRecursive;
                for (int i = 0; i < n1 + n2; i++) {
                    resultRecursive << ar3[i] << " ";
                }
                SetWindowText(hResultRecursive, resultRecursive.str().c_str());
            } else if (LOWORD(wParam) == 2) {
                SetWindowText(hEdit1, predefinedArray1);
                SetWindowText(hEdit2, predefinedArray2);
            }
            break;
        }

        case WM_DESTROY:
            PostQuitMessage(0);
            break;

        default:
            return DefWindowProc(hwnd, msg, wParam, lParam);
    }
    return 0;
}

void mergeArrays(int ar1[], int n1, int ar2[], int n2, int ar3[]) {
    int i = 0, j = 0, k = 0;

    // Loop ini digunakan untuk menggabungkan elemen-elemen dari kedua array sampai salah satu array habis
    for (i = 0, j = 0, k = 0; i < n1 && j < n2; k++) {
        // Kondisi ini memeriksa apakah elemen saat ini di ar1 lebih kecil dari elemen di ar2
        if (ar1[i] < ar2[j]) {
            ar3[k] = ar1[i];
            i++;
        } else {
            ar3[k] = ar2[j];
            j++;
        }
    }

    // Copy remaining elements from ar1, if any
    for (i = i; i < n1; i++, k++) {
        ar3[k] = ar1[i];
    }

    // Copy remaining elements from ar2, if any
    for (j = j; j < n2; j++, k++) {
        ar3[k] = ar2[j];
    }
}

void mergeRecursive(int ar1[], int n1, int ar2[], int n2, int ar3[]) {
     if (n1 > 0 && n2 > 0) {
        if (*ar1 < *ar2) {
            *ar3 = *ar1;
            mergeRecursive(ar1 + 1, n1 - 1, ar2, n2, ar3 + 1);
        } else {
            *ar3 = *ar2;
            mergeRecursive(ar1, n1, ar2 + 1, n2 - 1, ar3 + 1);
        }
    }
}
