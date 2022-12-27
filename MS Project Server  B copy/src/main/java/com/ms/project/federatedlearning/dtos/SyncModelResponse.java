package com.ms.project.federatedlearning.dtos;

import lombok.*;
import org.springframework.stereotype.Service;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
@EqualsAndHashCode
@ToString
public class SyncModelResponse {
    private String fileName;
    private String downloadUri;
    private Long size;


}
