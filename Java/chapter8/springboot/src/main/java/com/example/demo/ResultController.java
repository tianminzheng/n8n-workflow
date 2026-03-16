package com.example.demo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/results")
public class ResultController {

    @Autowired
    ResultService resultService;

    @PostMapping
    public ResponseEntity<ResultResponse> postResult(@RequestBody ResultRequest request) {
        // 验证result字段是否存在
        if (request.getResult() == null) {
            return ResponseEntity.badRequest().build();
        }

        ResultResponse response = resultService.processResult(request.getResult());
        if (response != null) {
            return ResponseEntity.ok(response);
        } else {
            return ResponseEntity.internalServerError().build();
        }
    }
}



//@RestController
//@RequestMapping("/api/results")
//public class ResultController {
//
//    @PostMapping
//    public ResponseEntity<ResultResponse> postResult(@RequestBody ResultRequest request) {
//        // 验证result字段是否存在
//        if (request.getResult() == null) {
//            return ResponseEntity.badRequest().build();
//        }
//
//        ResultResponse response = new ResultResponse("保存成功", true);
//        return ResponseEntity.ok(response);
//    }
//}