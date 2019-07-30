<?php $lg=$this->fields->luogu; ?>
<?php if (isset($lg)) { ?>
    <?php $dif=$id[$this->fields->luogu]; ?>
    <?php if ($dif==0){?>
        <span class="am-badge am-radius lg-bg-gray">尚无评定</span>
    <?php }else if ($dif==1){?>
        <span class="am-badge am-radius lg-bg-red">入门难度</span>
    <?php }else if ($dif==2){?>
        <span class="am-badge am-radius lg-bg-orange">普及-</span>
    <?php }else if ($dif==3){?>
        <span class="am-badge am-radius lg-bg-yellow">普及/提高-</span>
    <?php }else if ($dif==4){?>
        <span class="am-badge am-radius lg-bg-green">普及+/提高</span>
    <?php }else if ($dif==5){?>
        <span class="am-badge am-radius lg-bg-bluelight">提高+/省选-</span>
    <?php }else if ($dif==6){?>
        <span class="am-badge am-radius lg-bg-purple">省选/NOI-</span>
    <?php }else if ($dif==7){?>
        <span class="am-badge am-radius lg-bg-bluedark">NOI/NOI+/CTSC</span>
    <?php }?>
<?php }?>