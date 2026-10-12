
`timescale 1ns/1ps

module tb_and_gate;
    logic a;
    logic b;
    logic y;

    and_gate dut (
        .a(a),
        .b(b),
        .y(y)
    );

    initial begin
        $dumpfile("rtl/and_gate.vcd");
        $dumpvars(0, tb_and_gate);

        $display("time  a b | y");
        $monitor("%4t   %0b %0b | %0b", $time, a, b, y);

        a = 0; b = 0; #10;
        a = 0; b = 1; #10;
        a = 1; b = 0; #10;
        a = 1; b = 1; #10;

        $display("Simulation complete.");
        $finish;
    end
endmodule
