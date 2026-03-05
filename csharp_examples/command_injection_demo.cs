using System;
using System.Diagnostics;

class Demo
{
    static void Main(string[] args)
    {
        string userInput = args[0];

        Process.Start("cmd.exe", "/c dir " + userInput);
    }
}
