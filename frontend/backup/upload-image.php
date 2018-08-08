<?php
header('Cache-Control:no-cache,must-revalidate');   
header('Pragma:no-cache');   
header("Expires:0"); 
session_start();

if ( isset($_FILES["file"]["type"]) )
{
  $max_size = 8 * 500 * 1024; // 500 KB
  $destination_directory = "upload/";
  $validextensions = array("jpeg", "jpg", "png");

  $temporary = explode(".", $_FILES["file"]["name"]);
  $file_extension = end($temporary);

  // We need to check for image format and size again, because client-side code can be altered
  if ( (($_FILES["file"]["type"] == "image/png") ||
        ($_FILES["file"]["type"] == "image/jpg") ||
        ($_FILES["file"]["type"] == "image/jpeg")
       ) && in_array($file_extension, $validextensions))
  {
    if ( $_FILES["file"]["size"] < ($max_size) )
    {
      if ( $_FILES["file"]["error"] > 0 )
      {
        echo "<div class=\"alert alert-danger\" role=\"alert\">Error: <strong>" . $_FILES["file"]["error"] . "</strong></div>";
      }
      else
      {
        /*if ( file_exists($destination_directory . $_FILES["file"]["name"]) )
        {
          echo "<div class=\"alert alert-danger\" role=\"alert\">Error: File <strong>" . $_FILES["file"]["name"] . "</strong> already exists.</div>";
        }*/
        /*else
        {*/
          $sourcePath = $_FILES["file"]["tmp_name"];
          $targetPath = $destination_directory . $_FILES["file"]["name"];
          move_uploaded_file($sourcePath, $targetPath);

            $type = pathinfo($targetPath, PATHINFO_EXTENSION);
            $data = file_get_contents($targetPath);
            $base64 = base64_encode($data);
          $base64 = base64_encode($data);
          $data_string = "{\"data\":" . json_encode($base64) . "}";
          # echo $data_string;
          $ch = curl_init('http://149.28.128.228');
          curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");
          curl_setopt($ch, CURLOPT_POSTFIELDS, $data_string);
          curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
          curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));
          $result = curl_exec($ch);
          $decode = json_decode($result);

         # $type = gettype($result);
         #echo $type;
         # $dumpresult = var_dump(json_decode($result));
         # echo $dumpresult;
          # echo $result;
          echo "<div class=\"alert alert-success\" role=\"alert\">";
          echo "<p><strong>" . $decode->{'msg'}. "</strong></p>";
          echo " ";
          $aaaaa = $decode->{'ganimg'};
          $aaaaa = substr($decode->{'ganimg'},2,strlen($aaaaa)-3);
          # $aaaaa = base64_decode($aaaaa);
          # echo $aaaaa;
          # $image = imagecreatefromstring($aaaaa);
          # print $image;
//          header('Content-Type: image/jepg');
//          imagejpeg($image);
          # $newganimg = base64_decode($newganimg);
          $img='data:image/jpg;base64,'.$aaaaa;
          /*file_put_contents('upload/temp.jpg', $newganimg);
          echo "<img src=/"/upload/temp.jpg/" />";*/

          include "libchart/classes/libchart.php";
          $chart = new VerticalBarChart(500, 250);
          $dataSet = new XYDataSet();
          $s001 = $decode->{'predictions'}[0]->{'description'};
          $s001_n = round($decode->{'predictions'}[0]->{'probability'},3);
          $dataSet->addPoint(new Point($s001,$s001_n));
          $s002 = $decode->{'predictions'}[1]->{'description'};
          $s002_n = round($decode->{'predictions'}[1]->{'probability'},3);
          $dataSet->addPoint(new Point($s002,$s002_n));
          $s003 = $decode->{'predictions'}[2]->{'description'};
          $s003_n = round($decode->{'predictions'}[2]->{'probability'},3);
          $dataSet->addPoint(new Point($s003,$s003_n));
          $s004 = $decode->{'predictions'}[3]->{'description'};
          $s004_n = round($decode->{'predictions'}[3]->{'probability'},3);
          $dataSet->addPoint(new Point($s004,$s004_n));
          $s005 = $decode->{'predictions'}[4]->{'description'};
          $s005_n = round($decode->{'predictions'}[4]->{'probability'},3);
          $dataSet->addPoint(new Point($s005,$s005_n));
          $s006 = $decode->{'predictions'}[5]->{'description'};
          $s006_n = round($decode->{'predictions'}[5]->{'probability'},3);
          $dataSet->addPoint(new Point($s006,$s006_n));
          $s007 = $decode->{'predictions'}[6]->{'description'};
          $s007_n = round($decode->{'predictions'}[6]->{'probability'},3);
          $dataSet->addPoint(new Point($s007,$s007_n));

          $chart->setDataSet($dataSet);$chart->setTitle("Percentage");
          $chart->render("upload/sws3004.png");
          echo " <p>.</p> ";
          $file22 = "upload/sws3004.png";
          if($fp22 = fopen($file22,"rb", 0))
          {
              $gambar = fread($fp22,filesize($file22));
              fclose($fp22);
              $base64 = chunk_split(base64_encode($gambar));
              $encode = 'data:image/jpg;base64,' . $base64;
              echo "<img src = '{$encode}'/>";
          }
          echo "<p>" .$decode->{'predictions'}[0]->{'description'}." is about ". $decode->{'predictions'}[0]->{'probability'} ."</p>";
          echo "<p>" .$decode->{'predictions'}[1]->{'description'}." is about ". $decode->{'predictions'}[1]->{'probability'} ."</p>";
          echo "<p>" .$decode->{'predictions'}[2]->{'description'}." is about ". $decode->{'predictions'}[2]->{'probability'} ."</p>";
          echo "<p>" .$decode->{'predictions'}[3]->{'description'}." is about ". $decode->{'predictions'}[3]->{'probability'} ."</p>";
          echo "<p>" .$decode->{'predictions'}[4]->{'description'}." is about ". $decode->{'predictions'}[4]->{'probability'} ."</p>";
          echo "<p>" .$decode->{'predictions'}[5]->{'description'}." is about ". $decode->{'predictions'}[5]->{'probability'} ."</p>";
          echo "<p>" .$decode->{'predictions'}[6]->{'description'}." is about ". $decode->{'predictions'}[6]->{'probability'} ."</p>";
          # echo "<p>Image uploaded successful</p>";
          # echo "<p>File Name: <a href=\"". $targetPath . "\"><strong>" . $targetPath . "</strong></a></p>";
          # echo "<p>Type: <strong>" . $_FILES["file"]["type"] . "</strong></p>";
          # echo "<p>Size: <strong>" . round($_FILES["file"]["size"]/1024, 2) . " kB</strong></p>";
          # echo "<p>Temp file: <strong>" . $_FILES["file"]["tmp_name"] . "</strong></p>";
          echo "<p> . </p>";
          echo "<img src = '{$img}'/>";
          echo "</div>";
//        }
      }
    }
    else
    {
      echo "<div class=\"alert alert-danger\" role=\"alert\">The size of image you are attempting to upload is " . round($_FILES["file"]["size"]/1024, 2) . " KB, maximum size allowed is " . round($max_size/1024, 2) . " KB</div>";
    }
  }
  else
  {
    echo "<div class=\"alert alert-danger\" role=\"alert\">Unvalid image format. Allowed formats: JPG, JPEG, PNG.</div>";
  }
}

?>
