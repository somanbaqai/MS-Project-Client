package com.ms.project.federatedlearning.utils;

import org.springframework.core.io.UrlResource;
import org.springframework.stereotype.Service;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import org.springframework.core.io.Resource;

@Service
public class ModelTransferUtilService {
    private Path modelYMLFile;
    public Resource getModelYMLFileAsResource(String fileCode) throws IOException {
        Path dirPath = Paths.get("files-upload");

        Files.list(dirPath).forEach(file -> {
            if (file.getFileName().toString().startsWith(fileCode)) {
                modelYMLFile = file;
                return;
            }
        });

        if (modelYMLFile != null) {
            return new UrlResource(modelYMLFile.toUri());
        }

        return null;
    }
}
