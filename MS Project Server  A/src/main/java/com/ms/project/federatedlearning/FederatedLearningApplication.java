package com.ms.project.federatedlearning;

import org.apache.commons.io.FileUtils;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Base64;
import java.util.HashMap;
import java.util.Map;


@SpringBootApplication
public class FederatedLearningApplication {

    public static void main(String[] args) {
        SpringApplication.run(FederatedLearningApplication.class, args);
    }


}
