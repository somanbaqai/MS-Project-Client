package com.ms.project.federatedlearning.utils;

import javax.validation.Valid;
import javax.validation.constraints.NotBlank;

public class RequestHandler<T> {
    @Valid
    private T data;

//    @Valid
//    @NotBlank(message = "transaction Id may not be empty")
//    private String transactionId;


    public T getData() {
        return data;
    }

    public void setData(T data) {
        this.data = data;
    }


//    public String getTransactionId() {
//        return transactionId;
//    }
//
//    public void setTransactionId(String transactionId) {
//        this.transactionId = transactionId;
//    }


}