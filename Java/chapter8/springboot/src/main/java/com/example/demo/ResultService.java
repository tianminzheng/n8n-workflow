package com.example.demo;

import org.springframework.stereotype.Service;

@Service
public class ResultService {

    ResultResponse processResult(String result) {

        // TODO:根据具体的业务场景实现对账结果的保存
        return new ResultResponse("保存成功", true);
    }
}
