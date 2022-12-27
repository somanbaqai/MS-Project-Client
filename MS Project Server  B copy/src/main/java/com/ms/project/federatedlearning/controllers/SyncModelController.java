package com.ms.project.federatedlearning.controllers;

import com.ms.project.federatedlearning.dtos.SyncModelResponse;
import com.ms.project.federatedlearning.services.IModelSyncService;
import com.ms.project.federatedlearning.utils.ResponseHandler;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

import javax.validation.Valid;
import java.io.IOException;

@RestController
public class SyncModelController {

    private IModelSyncService modelSyncService;
    Logger logger = LoggerFactory.getLogger(SyncModelController.class);


    @Autowired
    public SyncModelController(IModelSyncService modelSyncService) {
        this.modelSyncService = modelSyncService;
    }
//
//    @GetMapping("/encode/model")
//    public ResponseHandler<SyncModelResponseDTO> getModel() throws IOException {
//        SyncModelResponseDTO response = modelSyncService.syncModel();
//        return new ResponseHandler<>(response);
//    }

    @PostMapping("/upload/model")
    public ResponseHandler<SyncModelResponse> uploadFile(@Valid @RequestParam("file") MultipartFile uploadedModelYMLFile)
            throws IOException {
        logger.info("Uploading Model from Server A");

        SyncModelResponse response = modelSyncService.syncModel(uploadedModelYMLFile);

        return new ResponseHandler<>(response);

    }




}
