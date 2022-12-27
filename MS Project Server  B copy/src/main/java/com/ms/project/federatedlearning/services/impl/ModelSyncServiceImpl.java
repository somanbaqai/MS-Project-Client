package com.ms.project.federatedlearning.services.impl;

import com.ms.project.federatedlearning.dtos.SyncModelResponse;
import com.ms.project.federatedlearning.services.IModelSyncService;
import com.ms.project.federatedlearning.utils.ModelSyncUtilService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.util.StringUtils;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;

@Service
public class ModelSyncServiceImpl implements IModelSyncService {

    private ModelSyncUtilService modelSyncUtilService;

    @Autowired
    public ModelSyncServiceImpl(ModelSyncUtilService modelSyncUtilService) {
        this.modelSyncUtilService = modelSyncUtilService;
    }

    ////    @Override
//    public SyncModelResponseDTO syncModel() throws IOException {
//        String encodedString = getBase64String();
//        return new SyncModelResponseDTO(encodedString);
//    }

//

    @Override
    public SyncModelResponse syncModel(MultipartFile model) throws IOException {
        String fileName = StringUtils.cleanPath(model.getOriginalFilename());
        long size = model.getSize();

        fileName = modelSyncUtilService.saveModelYMLFile(fileName, model);

        SyncModelResponse response = new SyncModelResponse();
        response.setFileName(fileName);
        response.setSize(size);
        response.setDownloadUri("/downloadFile/" + fileName);
        return response;
    }

}
