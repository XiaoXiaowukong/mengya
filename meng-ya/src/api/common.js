/**
 * 公共模块
 * date: 2019-08-07
 * by: zjfcool
 */
import {
  ACTIVITY_LIST,
} from './config';
import axios from './axios';

export function getActivityList({ared_id}) {
  return axios(`${ACTIVITY_LIST}/${ared_id}`);
}
