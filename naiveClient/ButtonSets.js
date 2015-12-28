/**
 * Created by gucheng on 12/28/15.
 */
const MK = require('react-native-material-kit');

const {
  MKButton,
  MKTextField,
  } = MK;

import {styles} from './Styles';

export const SetServerButton = MKButton.accentColoredButton()
  .withText('设置服务器')
  .build();

export const ServerAddressInput = MKTextField.textfieldWithFloatingLabel()
  .withPlaceholder('服务器地址：端口')
  .withStyle(styles.textfieldWithFloatingLabel)
  .withFloatingLabelFont({
    fontSize: 10,
    fontStyle: 'italic',
    fontWeight: '200',
  })
  .build();

export const ControllerButton = MKButton.coloredButton()
  .withStyle(styles.controllerButton)
  .build();

export const PlayPauseButton = MKButton.accentColoredButton()
  .withStyle(styles.playPauseButton)
  .build();

export const ShutdownButton = MKButton.accentColoredButton()
  .withText('关机')
  .build();