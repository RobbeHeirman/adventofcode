package day7.gates;

import day7.Wire;

import java.util.List;

public abstract class Gate {

    private List<Wire> fromWires;
    private Wire toWire;

    public void addFromWire(Wire fromWire) {
        fromWires.add(fromWire);
    }

    public void setToWire(Wire toWire) {
        this.toWire = toWire;
    }

    public abstract void applyGate();
}
