package com.ms.project.federatedlearning.dtos;

import lombok.*;

import javax.validation.constraints.NotBlank;
import javax.validation.constraints.NotNull;


@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@EqualsAndHashCode
@ToString
public class SyncModelRequestDTO {

    @NotNull(message = "model value parameter cannot be null")
    @NotBlank(message = "model value paramter cannot be blank")
    private String model;

}
