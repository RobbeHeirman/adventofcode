package core.java;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public interface Solution {
    default List<String> runInput(String filename) throws IOException {
         return Files.readAllLines(Path.of(filename));
    }

    Object solution1(List<String> input);
    default Object solution2(List<String> input){
        return "Not implemented yet";
    }

}
