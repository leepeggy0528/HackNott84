function exec1(command) {
    var ws= new COMObject("WScript.Shell");
    ws.run(command);
    }