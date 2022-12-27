package com.ms.project.federatedlearning.utils;

import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;
import java.io.InputStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;

@Service
public class ModelSyncUtilService {
    public String saveModelYMLFile(String fileName, MultipartFile multipartFile)
            throws IOException {
        Path uploadPath = Paths.get("files-upload");

        if (!Files.exists(uploadPath)) {
            Files.createDirectories(uploadPath);
        }

//        String fileCode = RandomStringUtils.randomAlphanumeric(8);

        try (InputStream inputStream = multipartFile.getInputStream()) {
            Path filePath = uploadPath.resolve( fileName);
            Files.copy(inputStream, filePath, StandardCopyOption.REPLACE_EXISTING);
        } catch (IOException ioe) {
            throw new IOException("Could not save file: " + fileName, ioe);
        }

        return fileName;
    }
}
