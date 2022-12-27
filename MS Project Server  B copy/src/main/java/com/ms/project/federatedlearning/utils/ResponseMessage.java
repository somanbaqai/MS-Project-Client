package com.ms.project.federatedlearning.utils;

public class ResponseMessage<T> {
    private String status;
    private T description;

    public ResponseMessage() {

    }

    public ResponseMessage(String status, T description) {
        this.status = status;
        this.description = description;
    }

    public ResponseMessage(T description) {
        this.description = description;
    }

    public ResponseMessage(String status) {
        this.status = status;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public T getDescription() {
        return description;
    }

    public void setDescription(T description) {
        this.description = description;
    }
}

