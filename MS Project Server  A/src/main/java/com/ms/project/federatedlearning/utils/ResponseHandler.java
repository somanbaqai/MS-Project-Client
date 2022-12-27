package com.ms.project.federatedlearning.utils;


import java.util.List;

public class ResponseHandler<T> {

    private T data;
    private ResponseMessage message;
    public T getData() {
        return data;
    }

    public ResponseHandler() {
        this.message = new ResponseMessage("200", "SUCCESS");
    }

    public ResponseHandler(T data) {
        this.message = new ResponseMessage("200", "SUCCESS");
        this.data = data;
    }

}
