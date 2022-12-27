package com.ms.project.federatedlearning.controllers;

import com.ms.project.federatedlearning.services.IModelTransferService;
//import com.sun.org.slf4j.internal.Logger;
//import com.sun.org.slf4j.internal.LoggerFactory;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.IOException;
//import java.util.logging.Logger;

@RestController
public class TransferModelController {
//    Logger logger = new Logger();
    Logger logger = LoggerFactory.getLogger(TransferModelController.class);

    private IModelTransferService modelTransferService;

    @Autowired
    public TransferModelController(IModelTransferService modelTransferService) {
        this.modelTransferService = modelTransferService;
    }

//    @PostMapping("/decode/model")
//    @RequestMapping(method = RequestMethod.POST, value = "/data")
////    public ResponseHandler<SyncModelResponseDTO> getModel(@Valid @RequestBody RequestHandler<SyncModelRequestDTO> requestHandler) throws IOException {
////        System.out.println("recived data:: " + requestHandler.getData() );
//        modelTransferService.transferModelToClient(requestHandler.getData());
////        return new ResponseHandler<>();
////    }

    @GetMapping("/download/model")
    public ResponseEntity<?> downloadFile() throws IOException {
        logger.info("Downloading Model from Server B");
        return modelTransferService.transferModelToClient();
    }


}
