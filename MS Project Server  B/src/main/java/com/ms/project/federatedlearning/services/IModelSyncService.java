package com.ms.project.federatedlearning.services;

import com.ms.project.federatedlearning.dtos.SyncModelResponse;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;

public interface IModelSyncService {

    SyncModelResponse syncModel(MultipartFile model) throws IOException;
}
