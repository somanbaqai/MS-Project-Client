package com.ms.project.federatedlearning.services;

import org.springframework.http.ResponseEntity;

import java.io.IOException;

public interface IModelTransferService {
    ResponseEntity transferModelToClient() throws IOException;
}
