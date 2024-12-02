package day7;

import day7.gates.Gate;

import java.util.Optional;

public class Wire {
    private final String name;

    private int value;
    private Gate fromGate;
    private Gate toGate;

    public Wire(String name) {
        this.name = name;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public void setFromGate(Gate fromGate) {

    }

    public void setToGate(Gate toGate) {

    }

    public Optional<Integer> getValue() {
        return Optional.of(value);
    }

    @Override
    public int hashCode() {
        return name.hashCode();
    }

    @Override
    public boolean equals(Object object) {
        if (this.getClass() != object.getClass()) {
            return false;
        }
        return this.name.equals(((Wire) object).name);
    }
}
