package com.ms.project.federatedlearning.services.impl;

import com.ms.project.federatedlearning.services.IModelTransferService;
import com.ms.project.federatedlearning.utils.ModelTransferUtilService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.io.Resource;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

import java.io.IOException;


@Service
public class ModelTransferServiceImpl implements IModelTransferService {

    private ModelTransferUtilService downloadUtilService;

    @Autowired
    public ModelTransferServiceImpl(ModelTransferUtilService downloadUtilService) {
        this.downloadUtilService = downloadUtilService;
    }

    //    @Override
//    public void transferModelToClient(SyncModelRequestDTO decodeModelRequestDTO) throws IOException {
//        decodeBase64AndSaveYamlModel(decodeModelRequestDTO.getModel());
////        int a = 10;
//    }

//    private void decodeBase64AndSaveYamlModel(String encodedString) throws IOException {
//        byte[] decodedBytes = Base64.getDecoder().decode(encodedString);
//        FileUtils.writeByteArrayToFile(new File("decoded-file-at-java.yml"), decodedBytes);
//
//    }

    @Override
    public ResponseEntity transferModelToClient() throws IOException {

        String filecode = "trainer.yml";
        Resource resource = null;
        try {
            resource = downloadUtilService.getModelYMLFileAsResource(filecode);
        } catch (IOException e) {
            return ResponseEntity.internalServerError().build();
        }

        if (resource == null) {
            return new ResponseEntity<>("File not found", HttpStatus.NOT_FOUND);
        }

        String contentType = "application/octet-stream";
        String headerValue = "attachment; filename=\"" + resource.getFilename() + "\"";

        return ResponseEntity.ok()
                .contentType(MediaType.parseMediaType(contentType))
                .header(HttpHeaders.CONTENT_DISPOSITION, headerValue)
                .body(resource);
    }

}
